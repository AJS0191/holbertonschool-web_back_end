var kue = require('kue');
var queue = kue.createQueue()

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

queue.process('sendNotification', (job, done) => {
    sendNotification(job.data.to, done);
})
