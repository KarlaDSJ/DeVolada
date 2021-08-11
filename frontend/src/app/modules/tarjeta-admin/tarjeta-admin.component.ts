import { Component, OnInit, Input } from '@angular/core';
import { IProducto } from "../../services/productos.service";

@Component({
  selector: 'app-tarjeta-admin',
  templateUrl: './tarjeta-admin.component.html',
  styleUrls: ['./tarjeta-admin.component.css']
})
export class TarjetaAdminComponent implements OnInit {

  @Input() producto: IProducto;

  constructor() { }

  ngOnInit(): void { }

}