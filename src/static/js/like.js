// セキュリティ関係で必要っぽい、ないとエラーが出る。
function getCookie(name){
    let cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        console.log(document.cookie);
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++){
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break; 
            }}
    }
    return cookieValue;
}

//サーバーからのレスポンスを受け取り、いいねの数を更新する関数
function addLike() {

    const csrftoken = getCookie('csrftoken');
    // いいねの状態をサーバーに送信するためのHTTPリクエストを送信
    fetch(`like/`, {
        method: 'POST', // POSTリクエストを送信
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
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
};

// いいねボタンの要素を取得
const addlikeButton = document.querySelector('#likeButton');

// いいねボタンがクリックされたときにaddLike関数を実行
addlikeButton.addEventListener("click", function(){
    addLike();
    // いいねボタンの色を赤に変更
    const heartIcon = document.querySelector('#likeButton i');
    if (heartIcon) {
        heartIcon.style.color = 'red';
    }
});

