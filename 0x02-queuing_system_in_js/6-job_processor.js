var kue = require('kue');
var queue = kue.createQueue()

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

queue.process('push_notification_code', (job, done) => {
    console.log(job);
    console.log(job.data);
    console.log(job.data.to)
    sendNotification(job.data.to, done);
})
