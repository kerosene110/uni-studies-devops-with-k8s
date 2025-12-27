const randomString = Math.random().toString(36)

const printLogLine = () => {
  const timestamp = new Date().toISOString()
  console.log(`${timestamp}: ${randomString}`)
}

printLogLine()
setInterval(printLogLine, 5000)
