from aiohttp import ClientSession
from typed import *
from bs4 import BeautifulSoup
from json import dumps, loads

class HttpClient(object):
    def __init__(self, url:str):
        self.url = url
        self.session = ClientSession()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }
    
    async def json(self)->Dict[str, Any]:
        """Get's json"""
        async with self.session.get(self.url, headers=self.headers) as response:
            return await response.json()
        
        
    async def html(self)->str:
        """Get's html"""
        async with self.session.get(self.url, headers=self.headers) as response:
            return await response.text(encoding='utf-8')
        
        
    async def soup(self)->BeautifulSoup:
        """Get's soup"""
        html = await self.html()
        return BeautifulSoup(html, 'lxml')
    
    async def links(self)->List[str]:
        """Get's links"""
        soup = await self.soup()
        response = []
        for link in soup.find_all('a', href=True):
            if link['href'].startswith('http'):
                response.append(link['href'])
            elif link['href'].startswith('/'):
                response.append(self.url + link['href'])
            else:
                continue
        return response
    
    async def images(self)->List[str]:
        """Get's images"""
        soup = await self.soup()
        response = []
        for img in soup.find_all('img', src=True):
            if img['src'].startswith('http'):
                response.append(img['src'])
            elif img['src'].startswith('/'):
                response.append(self.url + img['src'])
            else:
                continue
        return response
    
    async def scripts(self)->List[str]:
        """Get's scripts"""
        soup = await self.soup()
        response = []
        for script in soup.find_all('script', src=True):
            if script['src'].startswith('http'):
                response.append(script['src'])
            elif script['src'].startswith('/'):
                response.append(self.url + script['src'])
            else:
                continue
        return response
    
    async def styles(self)->List[str]:
        """Get's styles"""
        soup = await self.soup()
        response = []
        for style in soup.find_all('link', href=True):
            if style['href'].startswith('http'):
                response.append(style['href'])
            elif style['href'].startswith('/'):
                response.append(self.url + style['href'])
            else:
                continue
        return response
    
    async def headers(self)->Dict[str, Any]:
        """Get's headers"""
        async with self.session.get(self.url, headers=self.headers) as response:
            return dict(response.headers)
        
    async def status(self)->int:
        """Get's status"""
        async with self.session.get(self.url, headers=self.headers) as response:
            return response.status
        
    
class HttpResource(APIRouter):
    def __init__(self):
        super().__init__()
        
        @self.route('/json')
        async def json(url:AnyUrl):
            """Get's json"""
            return await HttpClient(url).json()
        
        @self.route('/html')
        async def html(url:AnyUrl):
            """Get's html"""
            return await HttpClient(url).html()
        
        
        @self.route('/content')
        async def content(url:AnyUrl):
            links = await HttpClient(url).links()
            images = await HttpClient(url).images()
            scripts = await HttpClient(url).scripts()
            styles = await HttpClient(url).styles()
            headers = await HttpClient(url).headers()
            status = await HttpClient(url).status()
            return {
                'links': links,
                'images': images,
                'scripts': scripts,
                'styles': styles,
                'headers': headers,
                'status': status
            }
            
            
