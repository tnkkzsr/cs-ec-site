document.getElementById('likeButton').addEventListener('click', function () {
    // いいねの状態をサーバーに送信するためのHTTPリクエストを送信
    fetch('/like', {
        method: 'POST', // POSTリクエストを送信
        headers: {
            'Content-Type': 'application/json',
            // いいねの情報をJSON形式で送信
        },
        body: JSON.stringify({
            action: 'like', // いいねを実行することをサーバーに伝える
            // 他の必要な情報があればここに追加
        })
    })
        .then(response => response.json()) // サーバーからの応答をJSON形式で解析
        .then(data => {
            // サーバーからの応答を元に、いいねの数を更新
            document.getElementById('likeCount').textContent = data.likes;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});