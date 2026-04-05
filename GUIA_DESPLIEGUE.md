# Guía de despliegue — Análisis de Enlace Químico

## Estructura de archivos
```
enlace_quimico/
├── app.py              ← Servidor Flask
├── requirements.txt    ← Dependencias Python
├── Procfile            ← Instrucción de arranque (nube)
└── templates/
    └── index.html      ← Interfaz web completa
```

---

## 1. Ejecución local (tu computadora)

### Requisitos
- Python 3.8 o superior instalado
- Conexión a internet (solo para instalar Flask la primera vez)

### Pasos
```bash
# 1. Instalar Flask
pip install flask

# 2. Entrar a la carpeta del proyecto
cd enlace_quimico

# 3. Correr el servidor
python app.py
```

Abre tu navegador en: **http://localhost:5000**

> El servidor debe estar corriendo para que cualquier usuario en tu
> red local pueda acceder. Comparte tu IP local (ej. 192.168.1.X:5000).

---

## 2. Despliegue en la nube — Railway (recomendado, gratuito)

Railway es la opción más sencilla: no requiere tarjeta de crédito
para el nivel gratuito y el despliegue toma menos de 5 minutos.

### Requisitos previos
- Cuenta en https://railway.app (puedes entrar con tu cuenta de GitHub)
- Git instalado en tu computadora

### Pasos

```bash
# 1. Inicializa un repositorio Git en la carpeta del proyecto
cd enlace_quimico
git init
git add .
git commit -m "primera versión"
```

```bash
# 2. Sube el proyecto a GitHub
#    (crea un repositorio nuevo en github.com y sigue sus instrucciones)
git remote add origin https://github.com/TU_USUARIO/enlace-quimico.git
git push -u origin main
```

En Railway:
1. Entra a https://railway.app → "New Project"
2. Selecciona "Deploy from GitHub repo"
3. Elige tu repositorio `enlace-quimico`
4. Railway detecta automáticamente que es una app Flask
5. En menos de 2 minutos tendrás una URL pública del tipo:
   **https://enlace-quimico-production.up.railway.app**

Esa URL la puedes compartir con cualquier usuario en el mundo,
sin que nadie necesite instalar nada.

---

## 3. Despliegue en la nube — Render (alternativa gratuita)

1. Entra a https://render.com → "New Web Service"
2. Conecta tu repositorio de GitHub
3. Configura:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `python app.py`
4. Haz clic en "Create Web Service"
5. Obtendrás una URL pública del tipo:
   **https://enlace-quimico.onrender.com**

> Nota: en el nivel gratuito de Render, el servidor "duerme"
> tras 15 minutos de inactividad y tarda ~30 segundos en
> despertar ante la primera visita.

---

## 4. Variables de entorno (opcional)

La app lee automáticamente la variable `PORT` que proveen
Railway y Render. No necesitas configurar nada adicional.

Para producción puedes agregar:
```
FLASK_ENV=production
```

---

## Resumen comparativo

| Opción         | Costo     | Tiempo de setup | URL pública | Límite gratuito      |
|----------------|-----------|-----------------|-------------|----------------------|
| Local          | Gratis    | 2 min           | No          | Sin límite           |
| Railway        | Gratis*   | 5 min           | Sí          | 500 hrs/mes          |
| Render         | Gratis    | 5 min           | Sí          | Duerme tras 15 min   |

*Railway ofrece $5 USD de crédito mensual gratuito, suficiente
para una aplicación de bajo tráfico.
