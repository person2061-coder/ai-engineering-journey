import requests
url="https://jsonplaceholder.typicode.com/posts"
b={
	"name":"harke",
	"age":"45",
	"dimag":"xaina",
}
c={
	"application-type":"application/json"
}
try:
	w=requests.post(url,headers=c,json=b, timeout=5)
	w.raise_for_status()
	y=w.json()
	print(f"it is stored in the id : {y['id']}")
	print(f"baula harke ko name nai :{y['name']}")
except Exception as e:
	print(f"error is : {e}")
