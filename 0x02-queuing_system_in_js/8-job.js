
function createPushNotificationsJobs(jobs, queue){ 
  console.log('hit function')   
  if (typeof(jobs) != Array){return new Error('Jobs is not an array')};
  jobs.forEach(job => {
      var push_notification_code3 = queue.create('push_notification_code3', {
        phoneNumber: job.phoneNumber,
        message: job.message,
      }).save( function(err){
        console.log(`Notification job created: ${push_notification_code3.id}`)
        }).on('complete', function(result){
          console.log(`Notification job ${push_notification_code3.id} completed`);
        }).on('failed', function(err){
          console.log(`Notification job ${push_notification_code3.id} failed: ${err}`)
        }).on('progress', function(progress, data){
          console.log(`Notification job ${push_notification_code3.id} ${progress}% complete`)
        })
  });
}
module.exports = createPushNotificationsJobs
