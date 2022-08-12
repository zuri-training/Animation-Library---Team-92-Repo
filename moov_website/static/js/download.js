function myFunction() {
    /* Get the text field */
    var copyLink = document.querySelector(".input-field");
  
    /* Select the text field */
    copyLink.select();
    copyLink.setSelectionRange(0, 999); //The amount of characters to select
  
    /* Copy the text inside the text field */
    navigator.clipboard.writeText(copyLink.value);
  
    /* Alert the copied text */
    confirm("Congratulations! You Copied the link, try pasting somewhere")
  
  
  }
  
  const downLoad = new File(['/Team-92-animation-library.zip'], 'Team92-Animation-library.zip', {
    type: 'text/plain',
  })
  
  function download() {
    const link = document.createElement('a')
    const url = URL.createObjectURL(downLoad)
  
    link.href = url
    link.download = downLoad.name
    document.body.appendChild(link)
    link.click()
  
    document.body.removeChild(link)
    window.URL.revokeObjectURL(url)
  }
  
  