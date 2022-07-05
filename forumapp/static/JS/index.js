$(document).ready(() => {
    setTimeout(() => {
        $('#welcome_heading').fadeIn(5000);
        $('#welcome_heading').removeClass('d-none');
    }, 500);

    let text = 'Asking question about coding made easy! Clear your all doubt about coding through iDiscuss.';
    let i = 0;

    text_animation = () => {
        if (i < text.length) {
            document.getElementById('welcome_text').innerHTML += text.charAt(i);
            i++;
            setTimeout(() => {
                text_animation();
            }, 40);
        }
    }

    setTimeout(() => {
        text_animation();
    }, 2500);


});