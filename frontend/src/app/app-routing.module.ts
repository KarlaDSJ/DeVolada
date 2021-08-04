import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InicioComponent } from './inicio/inicio.component';
import { ProductoComponent } from './producto/producto.component';
import { CarritoComponent } from './carrito/carrito.component';
import { DireccionComponent } from './direccion/direccion.component';
import { MetodoPagoComponent } from './metodo-pago/metodo-pago.component';
import { MisProductosComponent } from './mis-productos/mis-productos.component';
import { CompraFinalizadaComponent } from './compra-finalizada/compra-finalizada.component';
import { CrearResenaComponent } from './crear-resena/crear-resena.component';
import { VerResenasComponent } from './ver-resenas/ver-resenas.component';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  {path:  'login', component: LoginComponent},
  {path: 'carrito', component: CarritoComponent},
  {path: 'metodo-pago/:idCarrito/:idDir', component: MetodoPagoComponent}, 
  //Lleva el id del carrito y de la dirección
  {path: 'inicio', component: InicioComponent},
  {path: 'producto/:id', component: ProductoComponent}, //Lleva el id de producto
  {path: 'direccion/:idCarrito', component: DireccionComponent}, //Lleva el id del Carrito
  {path: 'mis-productos', component: MisProductosComponent},
  {path: 'compra-finalizada/:idCarrito/:idDir/:numTar', component: CompraFinalizadaComponent},
  //Lleva el id del carrito y de la dirección, el número de tarjeta de la compra
  {path: 'crear-resena', component: CrearResenaComponent},
  {path: 'ver-resenas', component: VerResenasComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
