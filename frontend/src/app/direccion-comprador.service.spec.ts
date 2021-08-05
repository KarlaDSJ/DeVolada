import { TestBed } from '@angular/core/testing';

import { DireccionCompradorService } from './direccion-comprador.service';

describe('DireccionCompradorService', () => {
  let service: DireccionCompradorService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DireccionCompradorService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
