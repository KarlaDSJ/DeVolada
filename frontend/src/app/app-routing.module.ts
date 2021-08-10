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
import { RegistrarComponent } from './registrar/registrar.component';
import { AuthGuard } from './auth.guard';
import { DireccionGuard } from './direccion.guard';
import { MetodoPagoGuard } from './metodo-pago.guard';
import { CompraFinalizadaGuard } from './compra-finalizada.guard';

const routes: Routes = [
  {path: 'registrar', component: RegistrarComponent},
  {path:  '', component: LoginComponent},
  {path: 'carrito', component: CarritoComponent, canActivate:[AuthGuard]},
  {path: 'metodo-pago', component: MetodoPagoComponent, canActivate:[AuthGuard, MetodoPagoGuard]},   
  {path: 'inicio', component: InicioComponent, canActivate:[AuthGuard]},
  {path: 'producto/:id', component: ProductoComponent, canActivate:[AuthGuard]}, //Lleva el id de producto
  {path: 'direccion', component: DireccionComponent, canActivate:[AuthGuard, DireccionGuard]}, //Lleva el id del Carrito
  {path: 'mis-productos', component: MisProductosComponent, canActivate:[AuthGuard]},
  {path: 'compra-finalizada/:idCompra', component: CompraFinalizadaComponent, canActivate:[AuthGuard, CompraFinalizadaGuard]},
  {path: 'crear-resena', component: CrearResenaComponent, canActivate:[AuthGuard]},
  {path: 'ver-resenas', component: VerResenasComponent, canActivate:[AuthGuard]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
