import { Component, OnInit } from '@angular/core';
import { IRegistrar } from '../registrar.service';
import { ActivatedRoute } from '@angular/router';
import { Router}   from '@angular/router';
import { RegistrarService } from "../registrar.service";
@Component({
  selector: 'app-registrar',
  templateUrl: './registrar.component.html',
  styleUrls: ['./registrar.component.css']
})
export class RegistrarComponent implements OnInit {
registrar: IRegistrar;
  
dataC = {
  
  correoC : '',
  nombreC : '',
  telefonoC : '',
  estadoC : '',
  ciudadC : '',
  coloniaC : '',
  cpC : '',
  calleC : '',
  numeroC : 0
  }
  dataV = {
  
    correoV : '',
    nombreV : '',
    telefonoV : '',
    estadoV : '',
    ciudadV : '',
    coloniaV : '',
    cpV : '',
    calleV : '',
    numeroV : 0,
    tarjetaV : ''
    }







  constructor(private _route:ActivatedRoute, private _registrarService: RegistrarService, private router: Router) { }

  ngOnInit(): void {
  }

  submit(){
    console.log(this.dataC)
    this._registrarService.registrarC(this.dataC).subscribe(response => {
      console.log(this.dataC)
      this.router.navigate(['/']);
    
    })

  }

  submitV(){
    this._registrarService.registrarV(this.dataV).subscribe(response => {
      
      this.router.navigate(['/']);
    
    })


  }


}
