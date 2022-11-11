var kue = require('kue');
var queue = kue.createQueue()

sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}

queue.process('sendNotification', (job, done){
    sendNotification(job.data.to, done);
})
