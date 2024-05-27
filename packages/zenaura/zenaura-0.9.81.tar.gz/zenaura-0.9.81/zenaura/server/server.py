from zenaura.client.page import Page 
from zenaura.client.hydrator import HydratorCompilerAdapter

compiler_adapter = HydratorCompilerAdapter()
class ZenauraServer:

    @staticmethod
    def hydrate_page(page : Page):
        return f"""

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="title" content="ZenUI Python" />
    <meta http-equiv="refresh"  />
    <meta
      name="description"
      content="Opensource solution for transitioning from traditional development to an API-first approach through mock APIs."
    />
    <script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>

 
  <script type="module" src="./zenaura/canvas.js"></script>
	<script type="py" src="./zenaura/main.py" config="./zenaura/config.json"></script>

    <link  rel="stylesheet" href="./zenaura/main.css">

    <title>Zenaura</title>
    
  </head>
  <body>
    <div id="root">
        {compiler_adapter.hyd_comp_compile_page(page)}
    </div>
  
  </body>

</html>
"""
        
