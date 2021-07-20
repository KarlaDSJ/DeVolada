import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CarritoComponent } from './carrito/carrito.component';
import { MetodoPagoComponent } from './metodo-pago/metodo-pago.component';

const routes: Routes = [
  {path: 'carrito', component: CarritoComponent},
  {path: 'metodo-pago', component: MetodoPagoComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
