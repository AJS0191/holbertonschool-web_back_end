const apiResolve = () => ({ status: 200, body: 'Success' });

const apiReject = () => new Error('');

export default function handleResponseFromAPI(promise) {
  promise.then(apiResolve);
  promise.catch(apiReject);
  promise.finally(() => {
    console.log('Got a response from the API');
  });
}
