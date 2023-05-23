let result;
let count;

function fishClick(i) {

    result++;
    count++;
    $(".schet-2").text(result);
    $(`.fish-${i}`).finish();
    $(`.fish-${i}`).remove();

}


$(function () {
    tableOfUser();
    let bn = 0;
    let makeBub;
    let fn = 0;
    let makeFi;

    $('.start').click(function () {

        $('.start').css('display', 'none');
        $('.tableOfUsers').css('display', 'none');

        count = 10;
        result = 0;
        $('.count-2').text(count);
        $('.schet-2').text(result);
        $('.end').css('display', 'none');
        count++;

        makeBub = setInterval(function () {
            let buble1 = new Buble(bn);
            buble1.makeBuble();
            bn++;
        }, 300);

        makeFi = setInterval(function () {
            let fish1 = new Fish(fn);
            fish1.makeFish();
            fn++;
        }, 3000);

    });

    $('[class!=fish]:first').click(function () {

        if (count == null || count == 0) {

            return 0;

        } else {

            count--;

            if (count == 0) {
                $('.start').css('display', 'block');
                $('.tableOfUsers').css('display', 'block');
                $('.end').css('display', 'block');

                tableOfUser();

                $('.endCount').text(result);


                $('.count-2').text(0);
                bn = 0;
                clearInterval(makeBub);
                fn = 0;
                clearInterval(makeFi);
                $('[class^=buble]').finish();
                $('[class^=buble]').remove();
                $('[class^=fish]').finish();
                $('[class^=fish]').remove();
            }

            $('.count-2').text(count);

        }
    });




    class Buble {

        constructor(num = Buble.getNum()) {

            this.heigth = Math.random() * 150;
            this.leftSide = Math.random() * (document.documentElement.clientWidth - this.heigth);
            this.num = num;
            this.way = document.documentElement.clientHeight - this.heigth;
            this.speed = (200 - this.heigth) * 100;

        }

        static getNum() { return 0; }

        makeBuble() {

            $('body').append('<img src="img/0_9cf4f_4a53c231_S.jpg" alt="" class="buble-' + this.num + '" height="' + this.heigth + '">');
            $(`.buble-${this.num}`).css('position', 'absolute');
            $(`.buble-${this.num}`).css('left', `${this.leftSide}px`);
            $(`.buble-${this.num}`).css('bottom', '0');
            $(`.buble-${this.num}`).animate({ 'bottom': `${this.way}` }, this.speed);
            $(`.buble-${this.num}`).animate({ 'opacity': '0' }, 1);

        }


    }

    class Fish {

        constructor(num = Fish.getNum()) {

            this.heigth = Math.random() * 150;
            this.pos = Math.floor(Math.random() * 2);
            this.startPos = Math.random() * (document.documentElement.clientHeight - this.heigth);

            this.startPos1 = Math.random() * (document.documentElement.clientHeight - this.heigth);
            this.startPos2 = Math.random() * (document.documentElement.clientHeight - this.heigth);
            this.startPos3 = Math.random() * (document.documentElement.clientHeight - this.heigth);

            this.num = num;
            this.way = (document.documentElement.clientWidth - this.heigth * 1.5) / 3;
            this.speed = Math.random() * 3000 + 1000;

        }

        static getNum() { return 0; }

        makeFish() {

            $('body').append('<img src="img/5a0ee9f24b2ef15fca41da84.png" alt="" class="fish-' + this.num + '" height="' + this.heigth + '" onclick="fishClick(' + this.num + ')">');
            $(`.fish-${this.num}`).css('position', 'absolute');
            $(`.fish-${this.num}`).css('top', `${this.startPos}`);

            if (this.pos === 1) {

                $(`.fish-${this.num}`).css('right', '0');
                $(`.fish-${this.num}`).animate({ 'right': `${this.way}`, 'top': `${this.startPos1}` }, this.speed);
                $(`.fish-${this.num}`).animate({ 'right': `${this.way * 2}`, 'top': `${this.startPos2}` }, this.speed);
                $(`.fish-${this.num}`).animate({ 'right': `${this.way * 3}`, 'top': `${this.startPos3}` }, this.speed);
                $(`.fish-${this.num}`).animate({ 'opacity': '0' }, 1);

            } else {

                $(`.fish-${this.num}`).css('left', '0');
                $(`.fish-${this.num}`).css('transform', 'scale(-1, 1)');
                $(`.fish-${this.num}`).animate({ 'left': `${this.way}`, 'top': `${this.startPos1}` }, this.speed);
                $(`.fish-${this.num}`).animate({ 'left': `${this.way * 2}`, 'top': `${this.startPos2}` }, this.speed);
                $(`.fish-${this.num}`).animate({ 'left': `${this.way * 3}`, 'top': `${this.startPos3}` }, this.speed);
                $(`.fish-${this.num}`).animate({ 'opacity': '0' }, 1);

            }
        }
    }
});


async function onSaveUser() {
    let username = $('#usernameid').val();
    let usercount = result;
    let obj = {
        name: username,
        count: usercount
    };
    // console.log(usercount);
    console.log(obj);


    let res = await fetch(`http://192.168.1.28:3000/users/${username}`);
    let result1 = await res.json();
    if (result1.length === 0) {
        fetch('http://192.168.1.28:3000/users/',
            {
                method: "POST",
                headers: {
                    'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(obj)

            });

    } else {
        fetch(`http://192.168.1.28:3000/users/${username}`,
            {
                method: "PUT",
                headers: {
                    'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(obj)

            });
    }

}

async function tableOfUser() {
    let res = await fetch(`http://192.168.1.28:3000/users`);
    let data = await res.json();
    let leng = 0;
    $('.tableOfUsers').empty();
    if (data.length > 10) {
        leng = 10;
    } else {
        leng = data.length;
    }
    data.sort((a, b) => (+a.count < +b.count) ? 1 : -1);
    for (let i = 0; i < leng; i++) {
        $('.tableOfUsers').append(`<p id="${i}">${i + 1} ${data[i].name} ${data[i].count}</p>`);
    }
};

