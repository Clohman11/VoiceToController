class Authentication {

  const request = require('request');

  const authOptions = {
    method: 'post',
    url: "https://api.symbl.ai/oauth2/token:generate",
    body: {
        type: "application",
        "appId": "4476436a32477647614d6b7934324d354a326d43616f766477444e6761573437",
        "appSecret": "5f61765762426c335a4d6f4e7862644a707270595675762d43303131704d44634f64667264544a4d6849684867437038466c7a6c586432316d4a6979496d6d35"
      },
      json: true
  };

  request(authOptions, (err, res, body) => {
    if (err) {
      console.error('error posting json: ', err);
      throw err
  }

   console.log(JSON.stringify(body, null, 2));
  });

  getAuth() {
    return(request(authOptions))
  }
}
