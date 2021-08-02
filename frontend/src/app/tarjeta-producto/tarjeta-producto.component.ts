import { Component, OnInit, Input } from '@angular/core';
import { IProducto } from "../productos.service";

@Component({
  selector: 'app-tarjeta-producto',
  templateUrl: './tarjeta-producto.component.html',
  styleUrls: ['./tarjeta-producto.component.css']
})
export class TarjetaProductoComponent implements OnInit {

  @Input() producto: IProducto;

  constructor() { }

  ngOnInit(): void { }

}
