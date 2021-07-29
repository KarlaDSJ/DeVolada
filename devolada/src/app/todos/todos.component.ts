import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.css']
})

export class TodosComponent implements OnInit {

  todos = [{
    "id" : 1010,
    "precio": 20000,
    "fotos":["https://images-na.ssl-images-amazon.com/images/I/71r1Zxx21sS._AC_SL1500_.jpg",
             "https://images-na.ssl-images-amazon.com/images/I/71bQhg8ykyS._AC_SL1500_.jpg",
             "https://images-na.ssl-images-amazon.com/images/I/51TzeazTjWS._AC_SL1500_.jpg"],
    "nombre": "Laptop",
    "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet cursus sit amet dictum. Quisque non tellus orci ac auctor. Quis vel eros donec ac odio tempor orci dapibus ultrices. Aliquam ut porttitor leo a diam sollicitudin tempor. Nibh ipsum consequat nisl vel. Non tellus orci ac auctor augue mauris. Et ultrices neque ornare aenean euismod elementum nisi quis. Facilisi morbi tempus iaculis urna id volutpat. Cras sed felis eget velit aliquet sagittis. Aliquam ultrices sagittis orci a scelerisque purus. Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.",
    "disponibles": 15
  },
  {
    "id" : 10,
    "precio": 5000,
    "nombre": "Celular",
    "fotos" : ["https://mixiaomipy.com/wp-content/uploads/2020/07/Xiaomi-Redmi-9-1.jpg",
               "https://mixiaomipy.com/wp-content/uploads/2020/07/xiaomi-redmi-9-32gb-dual-sim-gris-600x600.jpg"],
    "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet cursus sit amet dictum. Quisque non tellus orci ac auctor. Quis vel eros donec ac odio tempor orci dapibus ultrices. Aliquam ut porttitor leo a diam sollicitudin tempor. Nibh ipsum consequat nisl vel. Non tellus orci ac auctor augue mauris. Et ultrices neque ornare aenean euismod elementum nisi quis. Facilisi morbi tempus iaculis urna id volutpat. Cras sed felis eget velit aliquet sagittis. Aliquam ultrices sagittis orci a scelerisque purus. Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.",
    "disponibles": 2
  },
  {
    "id" : 200,
    "precio": 800.50,
    "nombre": "Monedero",
    "fotos":["https://images-na.ssl-images-amazon.com/images/I/61dO7WjfE-S._AC_SX679_.jpg",
             "https://images-na.ssl-images-amazon.com/images/I/6109Mqq96KS._AC_SX425_.jpg",
             "https://images-na.ssl-images-amazon.com/images/I/61kqJxojffS._AC_SX679_.jpg"],
    "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet cursus sit amet dictum. Quisque non tellus orci ac auctor. Quis vel eros donec ac odio tempor orci dapibus ultrices. Aliquam ut porttitor leo a diam sollicitudin tempor. Nibh ipsum consequat nisl vel. Non tellus orci ac auctor augue mauris. Et ultrices neque ornare aenean euismod elementum nisi quis. Facilisi morbi tempus iaculis urna id volutpat. Cras sed felis eget velit aliquet sagittis. Aliquam ultrices sagittis orci a scelerisque purus. Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.",
    "disponibles": 20
  },
  {
    "id" : 1014,
    "precio": 15000,
    "nombre": "Laptop",
    "fotos":["https://images-na.ssl-images-amazon.com/images/I/71r1Zxx21sS._AC_SL1500_.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/71bQhg8ykyS._AC_SL1500_.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/51TzeazTjWS._AC_SL1500_.jpg"],
    "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet cursus sit amet dictum. Quisque non tellus orci ac auctor. Quis vel eros donec ac odio tempor orci dapibus ultrices. Aliquam ut porttitor leo a diam sollicitudin tempor. Nibh ipsum consequat nisl vel. Non tellus orci ac auctor augue mauris. Et ultrices neque ornare aenean euismod elementum nisi quis. Facilisi morbi tempus iaculis urna id volutpat. Cras sed felis eget velit aliquet sagittis. Aliquam ultrices sagittis orci a scelerisque purus. Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.",
    "disponibles": 15
  },
  {
    "id" : 1010,
    "precio": 20000,
    "nombre": "Cámara",
    "fotos": ["https://images-na.ssl-images-amazon.com/images/I/61qMObWPAUL._AC_SL1000_.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/61Q8h4-CmGL._AC_SL1000_.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/61K2UQ1C6AL._AC_SL1000_.jpg"],
    "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet cursus sit amet dictum. Quisque non tellus orci ac auctor. Quis vel eros donec ac odio tempor orci dapibus ultrices. Aliquam ut porttitor leo a diam sollicitudin tempor. Nibh ipsum consequat nisl vel. Non tellus orci ac auctor augue mauris. Et ultrices neque ornare aenean euismod elementum nisi quis. Facilisi morbi tempus iaculis urna id volutpat. Cras sed felis eget velit aliquet sagittis. Aliquam ultrices sagittis orci a scelerisque purus. Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.",
    "disponibles": 5
  },
  {
    "id" : 1010,
    "precio": 20000,
    "fotos":["https://images-na.ssl-images-amazon.com/images/I/71r1Zxx21sS._AC_SL1500_.jpg",
             "https://images-na.ssl-images-amazon.com/images/I/71bQhg8ykyS._AC_SL1500_.jpg",
             "https://images-na.ssl-images-amazon.com/images/I/51TzeazTjWS._AC_SL1500_.jpg"],
    "nombre": "Laptop",
    "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet cursus sit amet dictum. Quisque non tellus orci ac auctor. Quis vel eros donec ac odio tempor orci dapibus ultrices. Aliquam ut porttitor leo a diam sollicitudin tempor. Nibh ipsum consequat nisl vel. Non tellus orci ac auctor augue mauris. Et ultrices neque ornare aenean euismod elementum nisi quis. Facilisi morbi tempus iaculis urna id volutpat. Cras sed felis eget velit aliquet sagittis. Aliquam ultrices sagittis orci a scelerisque purus. Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.",
    "disponibles": 15
  },
  {
    "id" : 200,
    "precio": 800.50,
    "nombre": "Monedero",
    "fotos":["https://images-na.ssl-images-amazon.com/images/I/61dO7WjfE-S._AC_SX679_.jpg",
             "https://images-na.ssl-images-amazon.com/images/I/6109Mqq96KS._AC_SX425_.jpg",
             "https://images-na.ssl-images-amazon.com/images/I/61kqJxojffS._AC_SX679_.jpg"],
    "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet cursus sit amet dictum. Quisque non tellus orci ac auctor. Quis vel eros donec ac odio tempor orci dapibus ultrices. Aliquam ut porttitor leo a diam sollicitudin tempor. Nibh ipsum consequat nisl vel. Non tellus orci ac auctor augue mauris. Et ultrices neque ornare aenean euismod elementum nisi quis. Facilisi morbi tempus iaculis urna id volutpat. Cras sed felis eget velit aliquet sagittis. Aliquam ultrices sagittis orci a scelerisque purus. Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.",
    "disponibles": 20
  },
  {
    "id" : 10,
    "precio": 5000,
    "nombre": "Celular",
    "fotos" : ["https://mixiaomipy.com/wp-content/uploads/2020/07/Xiaomi-Redmi-9-1.jpg",
               "https://mixiaomipy.com/wp-content/uploads/2020/07/xiaomi-redmi-9-32gb-dual-sim-gris-600x600.jpg"],
    "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet cursus sit amet dictum. Quisque non tellus orci ac auctor. Quis vel eros donec ac odio tempor orci dapibus ultrices. Aliquam ut porttitor leo a diam sollicitudin tempor. Nibh ipsum consequat nisl vel. Non tellus orci ac auctor augue mauris. Et ultrices neque ornare aenean euismod elementum nisi quis. Facilisi morbi tempus iaculis urna id volutpat. Cras sed felis eget velit aliquet sagittis. Aliquam ultrices sagittis orci a scelerisque purus. Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.",
    "disponibles": 2
  },
  {
    "id" : 1010,
    "precio": 20000,
    "nombre": "Cámara",
    "fotos": ["https://images-na.ssl-images-amazon.com/images/I/61qMObWPAUL._AC_SL1000_.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/61Q8h4-CmGL._AC_SL1000_.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/61K2UQ1C6AL._AC_SL1000_.jpg"],
    "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet cursus sit amet dictum. Quisque non tellus orci ac auctor. Quis vel eros donec ac odio tempor orci dapibus ultrices. Aliquam ut porttitor leo a diam sollicitudin tempor. Nibh ipsum consequat nisl vel. Non tellus orci ac auctor augue mauris. Et ultrices neque ornare aenean euismod elementum nisi quis. Facilisi morbi tempus iaculis urna id volutpat. Cras sed felis eget velit aliquet sagittis. Aliquam ultrices sagittis orci a scelerisque purus. Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.",
    "disponibles": 5
  },
  {
    "id" : 1014,
    "precio": 15000,
    "nombre": "Laptop",
    "fotos":["https://images-na.ssl-images-amazon.com/images/I/71r1Zxx21sS._AC_SL1500_.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/71bQhg8ykyS._AC_SL1500_.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/51TzeazTjWS._AC_SL1500_.jpg"],
    "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet cursus sit amet dictum. Quisque non tellus orci ac auctor. Quis vel eros donec ac odio tempor orci dapibus ultrices. Aliquam ut porttitor leo a diam sollicitudin tempor. Nibh ipsum consequat nisl vel. Non tellus orci ac auctor augue mauris. Et ultrices neque ornare aenean euismod elementum nisi quis. Facilisi morbi tempus iaculis urna id volutpat. Cras sed felis eget velit aliquet sagittis. Aliquam ultrices sagittis orci a scelerisque purus. Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.",
    "disponibles": 15
  }]

  responsiveOptions:any;

    constructor() {
        this.responsiveOptions = [
          {
            breakpoint: '1078px',
            numVisible: 3,
            numScroll: 2
          },
          {
            breakpoint: '840px',
            numVisible: 2,
            numScroll: 1
          },
          {
            breakpoint: '575px',
            numVisible: 1,
            numScroll: 1
          }];
    }


  ngOnInit(): void {

  }

}
