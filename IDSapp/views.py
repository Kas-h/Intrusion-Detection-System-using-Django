from django.shortcuts import render
from joblib import load

model = load('./savedModels/model.joblib')

protocol_type_mapping = {"tcp": 1, "udp": 2, "icmp": 0}
service_mapping = {"ftp_data": 19, "other": 41, "private": 46, "remote_job": 10, "http": 22, "telnet": 57, "mtp": 32, "gopher": 22}
flag_mapping = {"SF": 9, "S0": 5, "REJ": 1}

def predictor(request):
    if request.method == 'POST':
        #protocol_type = request.POST['protocol_type']
        #service = request.POST['service']
        #flag = request.POST['flag']
        protocol_type_str = request.POST['protocol_type']
        service_str = request.POST['service']
        flag_str = request.POST['flag']

        protocol_type = protocol_type_mapping.get(protocol_type_str, -1)
        service = service_mapping.get(service_str, -1)
        flag = flag_mapping.get(flag_str, -1)
        
        src_bytes = request.POST['src_bytes']
        dst_bytes = request.POST['dst_bytes']
        hot = request.POST['hot']
        count = request.POST['count']
        srv_count = request.POST['srv_count']
        diff_srv_rate = request.POST['diff_srv_rate']
        dst_host_count = request.POST['dst_host_count']
        dst_host_srv_count = request.POST['dst_host_srv_count']
        dst_host_same_srv_rate = request.POST['dst_host_same_srv_rate']
        dst_host_diff_srv_rate = request.POST['dst_host_diff_srv_rate']
        dst_host_same_src_port_rate = request.POST['dst_host_same_src_port_rate']
        dst_host_serror_rate = request.POST['dst_host_serror_rate']
        Test=model.predict([[protocol_type,service,flag, src_bytes, dst_bytes, hot, count, srv_count, diff_srv_rate, dst_host_count, dst_host_srv_count, dst_host_same_srv_rate, dst_host_diff_srv_rate, dst_host_same_src_port_rate, dst_host_serror_rate]])
        if Test[0]==0:
            Test = 'Anomaly'
        else:
            Test = 'Normal'
        return render(request,'main.html',{'result' : Test})
    return render(request,'main.html')

"""def formInfo(request):
    protocol_type = request.GET['protocol_type']
    service = request.GET['service']
    flag = request.GET['flag']
    src_bytes = request.GET['src_bytes']
    dst_bytes = request.GET['dst_bytes']
    hot = request.GET['hot']
    count = request.GET['count']
    srv_count = request.GET['srv_count']
    diff_srv_rate = request.GET['diff_srv_rate']
    dst_host_count = request.GET['dst_host_count']
    dst_host_srv_count = request.GET['dst_host_srv_count']
    dst_host_same_srv_rate = request.GET['dst_host_same_srv_rate']
    dst_host_diff_srv_rate = request.GET['dst_host_diff_srv_rate']
    dst_host_same_src_port_rate = request.GET['dst_host_same_src_port_rate']
    dst_host_serror_rate = request.GET['dst_host_serror_rate']
    Test=model.predict([[protocol_type,service,flag, src_bytes, dst_bytes, hot, count, srv_count, diff_srv_rate, dst_host_count, dst_host_srv_count, dst_host_same_srv_rate, dst_host_diff_srv_rate, dst_host_same_src_port_rate, dst_host_serror_rate]])
    if Test[0]==0:
        Test = 'Anomaly'
    else:
        Test = 'Normal'
    return render(request,'result.html',{'result' : Test})"""