const apiResolve = () => {
  console.log('Got a response from the API');
  return { status: 200, body: 'Success' };
};

const apiReject = () => {
  console.log('Got a response from the API');
  return new Error();
};

export default function handleResponseFromAPI(promise) {
  promise.then(apiResolve, apiReject);
}
