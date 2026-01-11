print("Operaciones")

num1 = float(input("Ingresar 1er numero: "))
num2 = float(input("Ingresar 2do numero: "))

Divicion = num1 / num2 if num2 != 0 else "Indefinido (no se puede dividir por 0)"

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicacion: {num1 * num2}")
print(f"Divicion: {Divicion}")

print("Par o Impar")

num = int(input("Ingrese un numero: "))

if num % 2 == 0:
    print(f"El numero {num} es PAR.")
else:
    print(f"El numero {num} es IMPAR.")



<!DOCTYPE html>

<html lang="es">

<head>

    <meta charset="UTF-8">

    <title>Feliz 2026 - Especial</title>

    <style>

        body, html { height: 100%; margin: 0; padding: 0; overflow: hidden; background: #000; }

        canvas { display: block; position: fixed; top: 0; left: 0; z-index: 1; }

        

        .modal {

            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;

            background: rgba(0,0,0,0.85); display: flex; align-items: center;

            justify-content: center; z-index: 10; opacity: 0;

            pointer-events: none; transition: opacity 0.6s;

        }

        .modal.show { opacity: 1; pointer-events: auto; }

        .modal-content {

            background: linear-gradient(135deg, #fff5e6 0%, #FF0303 100%);

            padding: 40px; border-radius: 20px; text-align: center;

            box-shadow: 0 0 30px rgba(255, 150, 100, 0.5);

            max-width: 450px; font-family: 'Segoe UI', sans-serif;

        }

        #cariModal .modal-content { font-family: 'Segoe Script', cursive, serif; color: #b32d56; }

        button {

            background: #ff4d88; color: white; border: none; padding: 12px 35px;

            border-radius: 30px; font-weight: bold; cursor: pointer; margin-top: 15px;

        }

        .carta-texto { text-align: left; line-height: 1.5; font-size: 1.15em; }

    </style>

</head>

<body>



    <audio id="musica" loop><source src="cancion.mp3" type="audio/mpeg"></audio>

    <audio id="fxExplosion" src="explosion.mp3" preload="auto"></audio>



    <div class="modal" id="startModal">

        <div class="modal-content">

            <h2 style="color: #ff4d88;">¡Sorprai!</h2>

            <p>Presiona el botón de abajo repito de avajoo...!</p>

            <button id="startBtn">Para tu</button>

        </div>

    </div>



    <div class="modal" id="cariModal">

        <div class="modal-content">

            <div class="carta-texto">

                <p>Feliz año wey!</p>

                <p>Te quiero mucho, pero a veces me dan ganas de donarte.</p>

                <p id="fechaCari"></p>

                <p>Que este 2026 ya seas papá .</p>

            </div>

            <button id="cerrarCari">Presiona aqui para ver mi carinho</button>

        </div>

    </div>



    <script>

        let chars, particles, canvas, ctx, w, h, current;

        let stars = [];

        let explosionesExtra = [];

        let duration = 4000;

        let str = ['FELIZ', 'AñO', 'NUEVO', '2026', '🐥']; 

        let animActiva = false;

        let finalizado = false;

        let modoGranFinal = false; 

        let pollitoFuegos = [];



        // --- SISTEMA DE SONIDO ---

        let sonidosTocados = {}; 

        let ultimoTiempoSonido = 0;

        const fxBase = document.getElementById('fxExplosion');



        function reproducirExplosion(volumen = 0.25) {

            const ahora = Date.now();

            if (fxBase && (ahora - ultimoTiempoSonido > 100)) {

                const sonido = fxBase.cloneNode();

                sonido.volume = volumen; 

                sonido.play().catch(e => { });

                ultimoTiempoSonido = ahora;

            }

        }



        const startModal = document.getElementById('startModal');

        const cariModal = document.getElementById('cariModal');

        const audio = document.getElementById('musica');



        function init() {

            canvas = document.createElement('canvas');

            document.body.append(canvas);

            ctx = canvas.getContext('2d');

            resize();

            createStars();

        }



        function resize() {

            w = canvas.width = innerWidth;

            h = canvas.height = innerHeight;

            particles = innerWidth < 400 ? 60 : 120;

        }



        function createStars() {

            stars = [];

            for(let i=0; i<150; i++) {

                stars.push({

                    x: Math.random() * w,

                    y: Math.random() * h,

                    size: Math.random() * 1.2,

                    blink: Math.random() * 0.05

                });

            }

        }



        function drawStars() {

            ctx.fillStyle = "white";

            stars.forEach(s => {

                ctx.globalAlpha = 0.4 + Math.sin(Date.now() * s.blink) * 0.4;

                ctx.beginPath();

                ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);

                ctx.fill();

            });

            ctx.globalAlpha = 1;

        }



        // --- CLASES DE EXPLOSIONES ---

        class ExplosionDecorativa {

            constructor(x, y, hue) {

                reproducirExplosion(0.2); 

                this.x = x; this.y = y;

                this.particles = [];

                this.hue = hue || Math.random() * 360;

                for(let i=0; i<30; i++) {

                    let angle = Math.random() * Math.PI * 2;

                    let speed = Math.random() * 4 + 2;

                    this.particles.push({

                        x: 0, y: 0, vx: Math.cos(angle) * speed, vy: Math.sin(angle) * speed, life: 1.0

                    });

                }

            }

            update() {

                this.particles.forEach(p => {

                    p.x += p.vx; p.y += p.vy; p.vy += 0.05; p.life -= 0.02;

                });

                this.particles = this.particles.filter(p => p.life > 0);

            }

            draw() {

                this.particles.forEach(p => {

                    ctx.fillStyle = `hsla(${this.hue}, 100%, 70%, ${p.life})`;

                    ctx.beginPath(); ctx.arc(this.x + p.x, this.y + p.y, 2, 0, Math.PI*2); ctx.fill();

                });

            }

        }



        class GranExplosionFinal {

            constructor(x, y) {

                reproducirExplosion(0.5);

                this.x = x; this.y = y;

                this.particles = [];

                for(let i=0; i<600; i++) {

                    let angle = Math.random() * Math.PI * 2;

                    let speed = Math.random() * 18 + 5; 

                    this.particles.push({

                        x: 0, y: 0, vx: Math.cos(angle) * speed, vy: Math.sin(angle) * speed,

                        life: 1.0, hue: Math.random() * 360, size: Math.random() * 3 + 1

                    });

                }

            }

            update() {

                this.particles.forEach(p => {

                    p.x += p.vx; p.y += p.vy; p.vy += 0.08; p.vx *= 0.96; p.vy *= 0.96;

                    p.life -= 0.008;

                });

                this.particles = this.particles.filter(p => p.life > 0);

            }

            draw() {

                if(this.particles.length > 500 && this.particles[0].life > 0.9) {

                      let grad = ctx.createRadialGradient(this.x, this.y, 0, this.x, this.y, w);

                      grad.addColorStop(0, 'rgba(255, 255, 255, 0.9)');

                      grad.addColorStop(1, 'transparent');

                      ctx.fillStyle = grad; ctx.fillRect(0,0,w,h);

                }

                this.particles.forEach(p => {

                    ctx.fillStyle = `hsla(${p.hue}, 100%, 60%, ${p.life})`;

                    ctx.beginPath(); ctx.arc(this.x + p.x, this.y + p.y, p.size, 0, Math.PI * 2); ctx.fill();

                });

            }

        }



        // --- SISTEMA DE PUNTOS PARA TEXTO PERSONALIZADO ---

        function getTextPoints(text, scale = 1) {

            let tmp = document.createElement('canvas');

            let size = 150; 

            tmp.width = size * text.length * 0.7; 

            tmp.height = size;

            let tCtx = tmp.getContext('2d');

            tCtx.font = 'bold ' + (size * 0.8) + 'px Arial';

            tCtx.fillStyle = 'white';

            tCtx.textBaseline = "middle"; 

            tCtx.textAlign = "center";

            tCtx.fillText(text, tmp.width/2, tmp.height/2);

            

            let data = tCtx.getImageData(0, 0, tmp.width, tmp.height);

            let pts = [];

            let step = 3; 

            for(let y=0; y<tmp.height; y+=step) {

                for(let x=0; x<tmp.width; x+=step) {

                    if(data.data[(y * tmp.width + x) * 4] > 128) {

                        pts.push([ (x - tmp.width/2) * scale, (y - tmp.height/2) * scale ]);

                    }

                }

            }

            return pts;

        }



        class FireTextFinal {

            constructor(text, yPos, colorHue) {

                reproducirExplosion(0.3);

                this.x = w / 2;

                this.y = yPos;

                this.t = 0;

                this.pts = getTextPoints(text, w < 500 ? 0.4 : 0.8);

                this.hue = colorHue;

            }

            update() {

                this.t += 0.015;

                this.opacity = this.t < 2.0 ? 1 : 1 - (this.t - 2.0);

            }

            draw() {

                if(this.opacity <= 0) return;

                ctx.globalAlpha = Math.max(0, this.opacity);

                let color = `hsl(${this.hue}, 100%, 60%)`;

                let expansion = Math.min(1, this.t * 3); 

                

                this.pts.forEach(p => {

                    let jitterX = (Math.random() - 0.5) * 2;

                    let jitterY = (Math.random() - 0.5) * 2;

                    let px = this.x + (p[0] * expansion) + jitterX;

                    let py = this.y + (p[1] * expansion) + jitterY;

                    

                    ctx.fillStyle = color;

                    ctx.beginPath(); 

                    ctx.arc(px, py, 1.2, 0, Math.PI*2); 

                    ctx.fill();

                });

                ctx.globalAlpha = 1;

            }

        }



        // --- SISTEMA DEL POLLITO (MODIFICADO PARA TRAZO) ---

        function makeChickPoints(isMain = false) {

            let c = document.createElement('canvas');

            let s = c.width = c.height = 350;

            let x = c.getContext('2d');

            

            // 1. Fondo blanco para contraste

            x.fillStyle = 'white';

            x.fillRect(0,0,s,s);

            

            // 2. Configurar el trazo negro (ESTO GENERA EL CONTORNO)

            x.strokeStyle = 'black';

            x.lineWidth = 14; // Trazo grueso para que las partículas tengan espacio

            x.lineCap = 'round';

            x.lineJoin = 'round';



            // --- DIBUJANDO EL POLLITO DE LA IMAGEN ---

            

            // Cuerpo y Cabeza

            x.beginPath();

            // Empezamos frente arriba

            x.moveTo(150, 80);

            // Curva cabeza hacia la derecha

            x.bezierCurveTo(220, 80, 240, 110, 240, 150);

            // Curva del pecho hacia abajo

            x.bezierCurveTo(240, 230, 200, 260, 150, 260);

            // Curva inferior hacia la colita

            x.bezierCurveTo(110, 260, 80, 230, 80, 180);

            // Colita levantada

            x.quadraticCurveTo(80, 150, 95, 150);

            // Regreso a la cabeza

            x.bezierCurveTo(100, 100, 120, 80, 150, 80);

            x.stroke();



            // Ala (es como una U o un 3 acostado en el centro)

            x.beginPath();

            x.moveTo(125, 180);

            x.bezierCurveTo(125, 220, 175, 220, 175, 180);

            x.stroke();



            // Pico (Triángulo redondeado)

            x.beginPath();

            x.moveTo(240, 130);

            x.lineTo(265, 140);

            x.lineTo(240, 155);

            x.stroke();



            // Patita Izquierda

            x.beginPath();

            x.moveTo(145, 260);

            x.quadraticCurveTo(135, 280, 125, 280); // Dedo atrás

            x.quadraticCurveTo(155, 280, 165, 260); // Dedo adelante

            x.stroke();

            

            // Patita Derecha

            x.beginPath();

            x.moveTo(180, 255);

            x.quadraticCurveTo(190, 275, 200, 275);

            x.stroke();



            // Ojo (Relleno negro, cuenta como trazo oscuro)

            x.fillStyle = 'black';

            x.beginPath(); 

            x.arc(200, 125, 10, 0, Math.PI * 2); 

            x.fill();



            // --- EXTRAYENDO PUNTOS ---

            let d = x.getImageData(0, 0, s, s);

            let pts = [];

            let limit = isMain ? 1200 : 500; // Más puntos para mejor definición

            let intentos = 0;

            

            while (pts.length < limit && intentos < 50000) {

                intentos++;

                let px = Math.random() * s; 

                let py = Math.random() * s;

                let o = (Math.floor(py) * s + Math.floor(px)) * 4;

                

                // IMPORTANTE: Buscamos píxeles OSCUROS (R < 128)

                // Esto asegura que solo tomamos el trazo negro

                if (d.data[o] < 128) { 

                    pts.push([px - s / 2, py - s / 2]);

                }

            }

            return pts;

        }



        function makeChar(c) {

            if (c === '🐥') return makeChickPoints(true);

            let tmp = document.createElement('canvas');

            let size = tmp.width = tmp.height = w < 400 ? 200 : 300;

            let tmpCtx = tmp.getContext('2d');

            tmpCtx.font = 'bold ' + size + 'px Arial';

            tmpCtx.fillStyle = 'white';

            tmpCtx.textBaseline = "middle"; tmpCtx.textAlign = "center";

            tmpCtx.fillText(c, size/2, size/2);

            let char2 = tmpCtx.getImageData(0,0,size,size);

            let char2particles = [];

            while(char2particles.length < particles){

                let x = size * Math.random(); let y = size * Math.random();

                let offset = (Math.floor(y) * size + Math.floor(x)) * 4;

                if(char2.data[offset]) char2particles.push([x - size/2, y - size/2]);

            }

            return char2particles;

        }



        function makeChars(t) {

            if (modoGranFinal) return;

            let actual = parseInt(t / duration) % str.length;

            if (current === actual) return;

            current = actual;

            chars = [...str[actual]].map(makeChar);

            if (str[actual] === '🐥' && !finalizado) {

                finalizado = true;

                lanzarCarta();

                crearFuegosPollito();

            }

        }



        function render(t) {

            if(!animActiva) return;

            requestAnimationFrame(render);

            ctx.fillStyle = 'rgba(0, 0, 5, 0.2)'; 

            ctx.fillRect(0, 0, w, h);

            drawStars();

            

            makeChars(t);

            if(chars && !modoGranFinal) {

                 chars.forEach((pts, i) => firework(t, i, pts));

            }

            

            pollitoFuegos.forEach(f => f.update());

            

            explosionesExtra.forEach((exp, idx) => {

                exp.update();

                exp.draw();

                if((exp.particles && exp.particles.length === 0) || (exp.opacity && exp.opacity <= 0)) {

                    explosionesExtra.splice(idx, 1);

                }

            });

        }



        function firework(t, i, pts) {

            let elapsed = t - i * 200;

            let id = i + chars.length * parseInt(elapsed - elapsed % duration);

            let progress = elapsed % duration / duration;

            

            let offsetX = Math.sin(id * 1.5) * (w * 0.05);

            let offsetY = Math.cos(id * 2.2) * (h * 0.1); 

            let dx = (i + 1) * w / (1 + chars.length) + offsetX;

            if (str[current] === '🐥') dx = w / 2;

            let targetY = h * 0.5 + offsetY;



            if (progress < 0.33) {

                let rocketP = progress * 3;

                ctx.fillStyle = 'white';

                circle(dx, h - (h - targetY) * rocketP, 1.5);

                if (progress < 0.05) { delete sonidosTocados[id]; }

            } else {

                if (!sonidosTocados[id]) {

                    reproducirExplosion();

                    sonidosTocados[id] = true;

                }

                let tExp = Math.min(1, Math.max(0, progress - 0.33) * 1.5);

                if (tExp > 0 && tExp < 0.05 && Math.random() > 0.8) {

                    explosionesExtra.push(new ExplosionDecorativa(dx, targetY));

                }

                let r = Math.max(0.1, 2.5 * (1 - tExp));

                let driftY = tExp * 30; 

                let hue = (str[current] === '🐥') ? 50 : (id * 70) % 360;

                let color = `hsl(${hue}, 100%, 70%)`;



                if(tExp < 0.3) {

                    let grad = ctx.createRadialGradient(dx, targetY, 0, dx, targetY, 200);

                    grad.addColorStop(0, `hsla(${hue}, 100%, 50%, 0.1)`);

                    grad.addColorStop(1, 'transparent');

                    ctx.fillStyle = grad; ctx.fillRect(0,0,w,h);

                }

                ctx.fillStyle = color;

                pts.forEach(xy => {

                    circle(tExp * xy[0] + dx, targetY + tExp * xy[1] + driftY, r);

                });

            }

        }



        function circle(x, y, r) {

            ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fill();

        }



        function crearFuegosPollito() {

            for (let i = 0; i < 8; i++) {

                setTimeout(() => {

                    let f = new PollitoFire();

                    pollitoFuegos.push(f);

                    explosionesExtra.push(new ExplosionDecorativa(f.x, f.y, 50));

                }, i * 700);

            }

        }



        class PollitoFire {

            constructor() {

                reproducirExplosion();

                this.x = Math.random() * (w * 0.8) + (w * 0.1);

                this.y = Math.random() * (h * 0.5) + (h * 0.1);

                this.t = 0;

                this.pts = makeChickPoints(false);

                this.size = Math.random() * 0.4 + 0.4;

                this.hue = 50;

            }

            update() {

                this.t += 0.012;

                if (this.t > 2.5) return;

                let opacity = this.t < 1.5 ? 1 : 1 - (this.t - 1.5);

                ctx.globalAlpha = Math.max(0, opacity);

                let currentY = this.y + (this.t * 15); 

                let color = `hsl(${this.hue}, 100%, 75%)`;

                this.pts.forEach(p => {

                    circle(this.x + p[0] * this.t * this.size, currentY + p[1] * this.t * this.size, 1.2, color);

                });

                ctx.globalAlpha = 1;

            }

        }



        function lanzarCarta() {

            const hoy = new Date();

            const f = `${String(hoy.getDate()).padStart(2,'0')}/${String(hoy.getMonth()+1).padStart(2,'0')}/${hoy.getFullYear()}`;

            document.getElementById('fechaCari').textContent = `Hoy es ${f} y sigo agradeciendo por tenerte.`;

            setTimeout(() => {

                cariModal.style.display = 'flex';

                setTimeout(() => cariModal.classList.add('show'), 10);

            }, 9000);

        }



        function lanzarGranFinal() {

            modoGranFinal = true; 

            // 1. Gran explosión blanca inicial

            explosionesExtra.push(new GranExplosionFinal(w/2, h/2));



            // Secuencia de textos

            setTimeout(() => {

                // "TE KIERO" - Rosa

                explosionesExtra.push(new FireTextFinal("TE KIERO", h * 0.25, 330));

            }, 1800);



            setTimeout(() => {

                // "MUSHO FEA" - Rosa oscuro

                explosionesExtra.push(new FireTextFinal("MUSHO FEA", h * 0.35, 340));

            }, 3000);



            // Pausa dramática... y luego el golpe de realidad



            setTimeout(() => {

                // "NO TE EMOCIONES" - Azul cian (frío)

                explosionesExtra.push(new FireTextFinal("NO TE EMOCIONES", h * 0.55, 180));

            }, 5000);



            setTimeout(() => {

                // "QUE ERA UNA TAREA" - Azul/Blanco

                explosionesExtra.push(new FireTextFinal("QUE ERA UNA TAREA XD", h * 0.65, 200));

            }, 6800);



            setTimeout(() => {

                // CORAZÓN AMARILLO FINAL

                explosionesExtra.push(new FireTextFinal("💛", h * 0.80, 50));

            }, 8500);

        }



        startBtn.onclick = () => {

            startModal.classList.remove('show');

            setTimeout(() => {

                startModal.style.display = 'none';

                init();

                animActiva = true;

                audio.play();

                requestAnimationFrame(render);

            }, 500);

        };



        cerrarCari.onclick = () => {

            cariModal.classList.remove('show');

            setTimeout(() => {

                cariModal.style.display = 'none';

                lanzarGranFinal(); 

            }, 500);

        };



        window.onload = () => { startModal.style.display = 'flex'; setTimeout(()=>startModal.classList.add('show'), 10); };

        window.onresize = resize;

    </script>

</body>

</html> 
