(()=>{
    const fileidcopy=document.getElementById('fileidcopy');
    const urlcopy=document.getElementById('urlcopy');
    const url = document.getElementById('url');
    const fileid = document.getElementById('fileid');
    const statusmessage = document.getElementById('status');
    

    urlcopy.addEventListener('click',()=>{
        window.navigator.clipboard.writeText(url.textContent);
        statusmessage.textContent='URL Copied to clipboard';
        });
    fileidcopy.addEventListener('click',()=>{
          window.navigator.clipboard.writeText(fileid.textContent);
          statusmessage.textContent='File ID Copied to clipboard';
    });

    // counter to remove the copied to clipboard text 
    setInterval(() => {
        statusmessage.textContent='';
    }, 5000);

})();