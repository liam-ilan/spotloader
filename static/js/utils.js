async function reqFile(url, method = 'GET', data = null) {
  // set fetch options
  const options = {
    method,
    headers: {
      'Content-Type': 'application/json; charset=utf-8'
    }
  }

  // add body if content exists
  if (data) {
    options.body = JSON.stringify(data)
  }

  // await the fetch from the url
  const res = await window.fetch(url, options)

  // return file as url
  return await res.blob()
}

// download blob
async function downloadFile(fileBlob){

  // create url from blob
  zipUrl = URL.createObjectURL(fileBlob)

  // create element to download blob
  const downloadElement = document.createElement('a')
  downloadElement.href = zipUrl
  downloadElement.download = 'songs.zip'

  // trigger user interaction (probably a better way to do this)
  document.body.appendChild(downloadElement)
  downloadElement.click()
  document.body.removeChild(downloadElement)

  // revoke URL
  URL.revokeObjectURL(zipUrl)
}

// download from spotify link
async function downloadFromLink(link) {
  let fileBlob = await reqFile('./api/v1/getsongs', 'POST', {link: link})
  downloadFile(fileBlob)
}