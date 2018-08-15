import requests
welfare_dict = {}
n=int(input("請輸入欲查詢數量"))
for i in range(1,n):
    r = requests.get('https://dataplus.cloud.org.tw/quiz_detail/'+str(i))
    #print(r)
    r_text = str(r.text)
    
    if str(r) != "<Response [200]>":
        print(i,str(r))
    else:
        start = r_text.find("獎勵機制")
        #print(start,end)
        if start == -1:
            print(i, "廠商未提供資料或網站有誤，請手動查詢")
        else:
            start = r_text.find("><",start)
            end = r_text.find("</p>",start)
            welfare_str = r_text[start+4:end].split("／")
            for j in welfare_str:
                if j in welfare_dict:
                    welfare_dict[j] += 1
                else:
                    welfare_dict[j] = 1
            print(i,r_text[start+4:end])
print(welfare_dict)