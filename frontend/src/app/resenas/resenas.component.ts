import { Component, Input, OnInit } from '@angular/core';
import { ResenasService, IResena } from "../resenas.service";

@Component({
  selector: 'app-resenas',
  templateUrl: './resenas.component.html',
  styleUrls: ['./resenas.component.css']
})
export class ResenasComponent implements OnInit {

  resenias: IResena[];
  @Input() idProducto: string;

  constructor(private _ResenasService: ResenasService) { }

  ngOnInit(): void {
    this._ResenasService.mostrar5Resenas(this.idProducto)
    .subscribe(data => { 
      this.resenias = data;
      console.log(data);
    });
  }

}
