# FBExtractor
  
Extract Facebook posts into markdown (.md)  
  
## Why?
  
I tried to creat an ebook (.epub) from my Facebook posts, but could not find a free service to do it.  
  
## How it works
  
1. Extracts my posts and comments from Facebook using this tool
1. This tool generates a markdown file
1. Convert markdown file into epub file use other service
    - ex. [でんでんコンバーター](https://conv.denshochan.com/)
    - [Markdown + Pandoc でお手軽に電子書籍を書く](https://qiita.com/sta/items/c88093b1b9da9c77b577)
　　
## How to use
  
1. [Register as a Facebook Developer](https://developers.facebook.com/docs/graph-api/get-started)
1. Open the Graph Explorer tool
1. Grant "user_posts" permission
1. Generate an Access Token
1. Set below environment variables
    1. user_token
        - Which you get at step 3
    1. outputfile
        - Path and file name of output markdown file
1. Run Extractor.py