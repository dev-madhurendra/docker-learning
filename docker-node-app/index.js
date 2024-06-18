const express = require('express')
const users = require('./data')

const port = 8082
const app = express()

app.get('/', (req, res) => {
    res.send("<a href='/users'>Get Users</a>")
})

app.get('/users', (req, res) => {
    res.json(users)
})

app.listen(port, () => {
    console.log(`Server is listening on port http://localhost:${port}`)
})
