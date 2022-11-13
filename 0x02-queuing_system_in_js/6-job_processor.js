var kue = require('kue');
var queue = kue.createQueue()

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
    console.log(job.data)
    const { phoneNumber, message } = job.data
    sendNotification(phoneNumber, message);
    done();
})
