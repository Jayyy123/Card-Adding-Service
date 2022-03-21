const express = require('express')
const http = require('http')

const app = express()

app.set('view engine','ejs')

app.get('/',(request,response)=>{
    response.render('index')
})


app.listen(3000)

