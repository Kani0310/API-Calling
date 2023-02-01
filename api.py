#get method in api calling
import requests
base_url = 'http:/universities.hipolabs.com/search?country=India'
response=requests.get(base_url)
universities=response.json()
print(unviersities)

for university in unviersities:
	print(university['state-province'])

	
#put method in api calling
import requests
# Making a PUT request
r = requests.put('https://httpbin.org/put', data ={'python': {'library': 'librarian'}})
print(r)
# print content of request
print(r.content)
	
	
	

#Post method in api calling
import requests
response = requests.post('https://httpbin.org/get', json={'python': {'library': 'librarian'}})
print(response.request.body)
                      



#delete method in api calling
import requests
del_page = requests.delete('https://www.youtube.com/', data ={'key':'value'})
print("Specified page is deleted successfully, the success code is = ", del_page)
