//making the tumblr API app in JS and praying that it works


// Authenticate via API Key
var tumblr = require('tumblr.js');
var client = tumblr.createClient({
    consumer_key: 'uzZ82cyrSJZTSDStkchPypRyMTb0V9M2v4I9n0FMc6NAKt49Y6',
    consumer_secret:                             'xKV5kEbPt7dEagFaINnMK4HguE9IS272AWKC3vuK548hQeZqbF',
    token:  'pfkUVSmccshMtZfxsegy8OqdmK9YNAN2Xnn9yNmCkZCKYnitES',         token_secret:
   'qPtdm6xkqNMUzlOXYv2Qx8qFjOO89vFMGqLhf3ydEKga2CKwSl'});


for(var i=0; i<=2000; i+=20) {
    
    // Make the request
    client.blogPosts("toptextposts.tumblr.com",{limit: 20, offset:i}, function(err, data) {
        L = [];
        posts = data['body'];
        for(var i=0; i<posts.length; i++) {
            specific_post = posts[i];
            if(specific_post['type'] == 'text') {
			    L.push(specific_post['body']);
            };
        };
        console.log(L);
    });
};


