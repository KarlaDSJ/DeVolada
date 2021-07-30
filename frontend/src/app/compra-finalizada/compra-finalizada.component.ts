import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-compra-finalizada',
  templateUrl: './compra-finalizada.component.html',
  styleUrls: ['./compra-finalizada.component.css']
})
export class CompraFinalizadaComponent implements OnInit {

  comprador = "Yo merengues";
  dir = "Main St 1234, Evolución, Nezahualcóyotl, Ciudad de México, 12345";
  imagenP = "https://i.pinimg.com/originals/1a/ac/af/1aacaff36d04df6b1d189c6f22b4ceb9.jpg";
  nombreP = "Nombre del producto";
  cant = 1;

  listaP = [
    {imagenp: "https://i.pinimg.com/originals/1a/ac/af/1aacaff36d04df6b1d189c6f22b4ceb9.jpg", 
    nombre: "Shiba bb", cant: 1, idP: 12, precioP: 500, disp: 4},
    {imagenp: "https://demascotas.info/wp-content/uploads/2018/01/dog-3098176_1280.jpg", 
    nombre: "Shiba bb", cant: 1, idP: 13, precioP: 800, disp: 1}    
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
