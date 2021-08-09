import urllib.request, urllib.error, urllib.parse

url = 'https://pme.estadao.com.br/blogs/blog-do-empreendedor/negocio-de-impacto-atua-na-identificacao-de-superdotacao-e-autismo/'

response = urllib.request.urlopen(url)
webContent = response.read()

print(webContent[0:300])