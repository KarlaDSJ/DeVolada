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

  constructor() { }

  ngOnInit(): void {
  }

}
