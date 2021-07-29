import { Component, OnInit} from '@angular/core';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-producto',
  templateUrl: './producto.component.html',
  styleUrls: ['./producto.component.css']
})


export class ProductoComponent implements OnInit {

  producto: any = {
      "id" : 1010,
      "precio": 20000,
      "fotos":["https://images-na.ssl-images-amazon.com/images/I/71r1Zxx21sS._AC_SL1500_.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/71bQhg8ykyS._AC_SL1500_.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/51TzeazTjWS._AC_SL1500_.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/71r1Zxx21sS._AC_SL1500_.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/71bQhg8ykyS._AC_SL1500_.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/51TzeazTjWS._AC_SL1500_.jpg"],
      "nombre": "Laptop",
      "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet cursus sit amet dictum. Quisque non tellus orci ac auctor. Quis vel eros donec ac odio tempor orci dapibus ultrices. Aliquam ut porttitor leo a diam sollicitudin tempor. Nibh ipsum consequat nisl vel. Non tellus orci ac auctor augue mauris. Et ultrices neque ornare aenean euismod elementum nisi quis. Facilisi morbi tempus iaculis urna id volutpat. Cras sed felis eget velit aliquet sagittis. Aliquam ultrices sagittis orci a scelerisque purus. Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.",
      "disponibles": 15
    };

  id: any = "";
  responsiveOptions:any;

  constructor(private _route:ActivatedRoute) {
    this.responsiveOptions = [
      {
          breakpoint: '1024px',
          numVisible: 1,
          numScroll: 1
      }
    ];
  }

  ngOnInit(): void {
    this.id = this._route.snapshot.paramMap.get('id');
    console.log(this.id);
  }

}
