var kue = require('kue');
var queue = kue.createQueue()

blacklisted = ['4153518780', '4153518781']

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);
    if (phoneNumber in blacklisted){
        throw new Error(`Phone number ${phoneNumber} is blacklisted`);
    }
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
    console.log(job.data)
    const { phoneNumber, message } = job.data
    sendNotification(phoneNumber, message);
    done();
})
