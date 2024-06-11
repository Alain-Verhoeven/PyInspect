function getCurrentURL () {
    var getUrl = window.location;
    return getUrl.origin
}

async function sendmail() {

    console.log(`token = ${localStorage.getItem("token")}`)
    alert(getCurrentURL())
    alert('start send mail');
    const email = document.getElementById("email").innerText;
    subject = 'testmail';
    body = 'dit is een test mail';
    sender = 'alain.verhoeven1@gmail.com'

    if(email === 'veerleke402@hotmail.com'){
        subject='Speciale boodschap'
        body='Jij bent mijn liefke'
    }
    if(email === 'adriaan.vanerps@gmail.com'){
        subject='Speciale boodschap'
        body='Het mankementen team wenst je een prettige dag verder !'
    }
    if(email === 'alain.verhoeven1@gmail.com'){
        subject='Beste vriend'
        body='Ga je ook voor mij stemmen?'
    }
    if(email === 'yvan.verhoeven@telenet.be'){
        subject='Beste vriend'
        body='Ga je ook voor mij stemmen?'
    }

    alert("B");
    console.log(email)
    console.log(subject)
    console.log(body)
    console.log(sender)

    //const response = await fetch('http://tvsistop.duckdns.org:8000/send-email/', {
    test = `${getCurrentURL()}/send-email/`
    console.log(test)

    const response = await fetch(`${getCurrentURL()}/send-email/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, subject, body,sender})
    });

    console.log('verzonden')
    const result = await response.json();
    alert(result.message);
}