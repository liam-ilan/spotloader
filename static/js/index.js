linkInput = document.getElementById('link-input')
downloadButton = document.getElementById('download-button')
loadingIndicator = document.getElementById('loading')

// hides and shows element while allowing for animation
function hideElement(el) {
  el.style.display = 'none'
}

function showElement(el) {
  el.style.display = 'inline-block'
}

downloadButton.addEventListener('click', async function(e) {
  hideElement(downloadButton)
  showElement(loadingIndicator)
  
  await downloadFromLink(linkInput.value)

  showElement(downloadButton)
  hideElement(loadingIndicator)

  linkInput.value = ''
})