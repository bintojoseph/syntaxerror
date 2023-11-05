const {MongoClient} = require('mongodb')

const state = {
    db:null
}

module.exports.connect = function(done){
    const url='mongodb://localhost:27017'
    const dbname='restaurant'

    MongoClient.connect(url,(err,data)=>{
        if(err) return done(err)

        state.db=data.db(dbname)
        console.log('connected')

        done()
    })

    
}

module.exports.get=function(){
    return state.db
}