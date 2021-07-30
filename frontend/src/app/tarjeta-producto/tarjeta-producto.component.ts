import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-tarjeta-producto',
  templateUrl: './tarjeta-producto.component.html',
  styleUrls: ['./tarjeta-producto.component.css']
})
export class TarjetaProductoComponent implements OnInit {

  @Input() producto: any = {};

  constructor() { }

  ngOnInit(): void {
  }

}
