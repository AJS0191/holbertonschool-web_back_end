var kue = require('kue');
var queue = kue.createQueue()

var jobData = {
  phoneNumber: 'string',
  message: 'string',
}

var push_notification_code = queue.create('push_notification_code', {
  phoneNumber: 'string',
  message: 'string',
}).save( function(err){
  console.log(`Notification job created: ${push_notification_code.id}`)
}).on('complete', function(result){
  console.log('Notification job completed');
}).on('failed', function(err){
  console.log('Notification job failed')
})
