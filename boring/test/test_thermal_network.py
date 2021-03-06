from __future__ import print_function, division, absolute_import

import unittest

import numpy as np
from openmdao.api import Problem, Group, IndepVarComp, n2, view_connections
from openmdao.utils.assert_utils import assert_check_partials, assert_near_equal

from lcapy import R, LSection, Series

from boring.util.spec_test import assert_match_spec
from boring.src.sizing.thermal_network import Circuit, Radial_Stack, thermal_link


class TestCircuit(unittest.TestCase):



    def setUp(self):
        p1 = self.prob = Problem(model=Group())
        p1.model.add_subsystem('circ', subsys=Circuit())

        p1.setup()

        Rexe = 0.0000001
        Rexc = 0.0000001
        Rwe = 0.2545383947014702
        Rwke = 0.7943030881649811
        Rv = 8.852701208752846e-06
        Rintere = 0.00034794562965549745
        Rinterc = 0.00017397281482774872
        Rwkc = 0.39715154408249054
        Rwka = 744.3007160198263
        Rwa = 456.90414284754644
        Rwc = 0.1272691973507351
        self.prob['circ.Rex_e.R'] = Rexe
        self.prob['circ.Rex_c.R'] = Rexc
        self.prob['circ.Rwe.R'] = Rwe
        self.prob['circ.Rwke.R'] = Rwke
        self.prob['circ.Rv.R'] = Rv
        self.prob['circ.Rinter_e.R'] = Rintere
        self.prob['circ.Rinter_c.R'] = Rinterc
        self.prob['circ.Rwkc.R'] = Rwkc
        self.prob['circ.Rwka.R'] = Rwka
        self.prob['circ.Rwa.R'] = Rwa
        self.prob['circ.Rwc.R'] = Rwc
        self.prob['circ.Rex_e.T_in'] = 100
        self.prob['circ.Rex_c.T_out'] = 20

        p1.run_model()
        #p1.model.list_outputs(values=True, prom_name=True)

 
    def test_resistance(self):

        Rexe = 0.0000001
        Rexc = 0.0000001
        Rwe = 0.2545383947014702
        Rwke = 0.7943030881649811
        Rv = 8.852701208752846e-06
        Rintere = 0.00034794562965549745
        Rinterc = 0.00017397281482774872
        Rwkc = 0.39715154408249054
        Rwka = 744.3007160198263
        Rwa = 456.90414284754644
        Rwc = 0.1272691973507351

        Rtot = (R(Rexe) + (R(Rwa) | R(Rwe) + (R(Rwka)|R(Rwke)+R(Rintere)+R(Rv)+R(Rinterc)+R(Rwkc))+ R(Rwc))+ R(Rexc))

        print(Rtot.simplify())
        ans = 16731692103737332239244353077427184638278095509511778941./10680954190791611228174081719413008273307025000000000000.

        Rtot2 = (self.prob.get_val('circ.n1.T')-self.prob.get_val('circ.n8.T'))/self.prob.get_val('circ.Rex_c.q')

        assert_near_equal(Rtot2, ans, tolerance=1.0E-5)

        draw = False # plot the thermal network
        if draw:
            Rtot.draw('Thermal_Network.pdf')

    def test_link(self):

        p2 = self.prob2 = Problem(model=Group())
        p2.model.add_subsystem('evap', Radial_Stack(n_in=0, n_out=1),
                               promotes_inputs=['D_od','t_wk','t_w','k_wk','k_w','D_v','L_adiabatic','alpha']) # promote shared values (geometry, mat props)
        p2.model.add_subsystem('cond', Radial_Stack(n_in=1, n_out=0),
                               promotes_inputs=['D_od','t_wk','t_w','k_wk','k_w','D_v','L_adiabatic','alpha'])

        thermal_link(p2.model,'evap','cond')

        p2.model.set_input_defaults('k_w',11.4)

        p2.setup(force_alloc_complex=True)

        Rexe = 0.0000001
        Rexc = 0.0000001
        # Rwe = 0.2545383947014702
        # Rwke = 0.7943030881649811
        # Rv = 8.852701208752846e-06
        # Rintere = 0.00034794562965549745
        # Rinterc = 0.00017397281482774872
        # Rwkc = 0.39715154408249054
        # Rwka = 744.3007160198263
        # Rwa = 456.90414284754644
        # Rwc = 0.1272691973507351
        self.prob2['evap.Rex.R'] = Rexe
        # self.prob2['evap.Rw.R'] = Rwe
        # self.prob2['evap.Rwk.R'] = Rwke
        # self.prob2['evap.Rinter.R'] = Rintere
        # self.prob2['cond.Rinter.R'] = Rinterc
        # self.prob2['cond.Rwk.R'] = Rwkc
        # self.prob2['cond.Rw.R'] = Rwc
        self.prob2['cond.Rex.R'] = Rexc

        self.prob2['cond.L_flux'] = 0.02
        self.prob2['evap.L_flux'] = 0.01
        self.prob2['L_adiabatic'] = 0.03
        # self.prob2['h_fg'] = 
        # self.prob2['T_hp'] =
        # self.prob2['v_fg'] =
        # self.prob2['R_g'] =
        # self.prob2['P_v'] =
        # self.prob2['k_l'] = 
        self.prob2['t_wk'] = 0.00069
        self.prob2['t_w'] = 0.0005
        self.prob2['D_od'] = 0.006
        self.prob2['k_w'] = 11.4
        self.prob2['epsilon'] = 0.46
        self.prob2['D_v'] = 0.00362
        self.prob2['L_eff'] = (self.prob2['cond.L_flux']+self.prob2['evap.L_flux'])/2.+self.prob2['L_adiabatic']
        # self.prob2['k_wk'] = (1-self.prob2['epsilon'])*self.prob2['k_w']+self.prob2['epsilon']*self.prob2['k_l'] # Bridge
        # self.prob2['A_cond'] = np.pi*self.prob2['D_od']*self.prob2['L_cond']
        # self.prob2['A_evap'] =  np.pi*self.prob2['D_od']*self.prob2['L_evap']
        # self.prob2['A_w'] = np.pi*((self.prob2['D_od']/2.)**2-(self.prob2['D_od']/2.-self.prob2['t_w'])**2)
        # self.prob2['A_wk'] = np.pi*((self.prob2['D_od']/2.-self.prob2['t_w'])**2-(self.prob2['D_v']/2.)**2)
        # self.prob2['A_inter'] = np.pi*self.prob2['D_v']*self.prob2['L_evap']

        #self.prob2['evap_bridge.Rv.R'] = Rv
        #self.prob2['evap_bridge.Rwka.R'] = Rwka
        #self.prob2['evap_bridge.Rwa.R'] = Rwa
        self.prob2['evap.Rex.T_in'] = 100
        self.prob2['cond.Rex.T_in'] = 20

        p2.run_model()
        # p2.model.list_inputs(values=True, prom_name=True)
        # p2.model.list_outputs(values=True, prom_name=True)
        # n2(p2)
        # view_connections(p2)

        Rtot3 = (self.prob2.get_val('evap.n1.T')-self.prob2.get_val('cond.n1.T'))/np.abs(self.prob2.get_val('cond.Rex.q'))

        ans = 16731692103737332239244353077427184638278095509511778941./10680954190791611228174081719413008273307025000000000000.
        assert_near_equal(Rtot3, ans, tolerance=3.0E-5)

    def test_two_port(self):

        Rexe = 0.0000001
        Rexc = 0.0000001
        Rwe = 0.2545383947014702
        Rwke = 0.7943030881649811
        Rv = 8.852701208752846e-06
        Rintere = 0.00034794562965549745
        Rinterc = 0.00017397281482774872
        Rwkc = 0.39715154408249054
        Rwka = 744.3007160198263
        Rwa = 456.90414284754644
        Rwc = 0.1272691973507351

        Rtota= R(Rexe) + (R(Rwa) | R(Rwe) + (R(Rwka)|R(Rwke)+R(Rintere)+R(Rv)+R(Rinterc)+R(Rwkc))+ R(Rwc))+ R(Rexc)
        #                                                                                                   |         |
        Rtot = R(Rexe) + (R(Rwa) | R(Rwe) + (R(Rwka)|R(Rwke)+R(Rintere)+R(Rv)+R(Rinterc)+R(Rwkc))+ R(Rwc)) + (R(1.6+Rexc) | (R(Rexe) + (R(Rwa) | R(Rwe) + (R(Rwka)|R(Rwke)+R(Rintere)+R(Rv)+R(Rinterc)+R(Rwkc))+ R(Rwc))+ R(Rexc)))
        print(Rtot.simplify())
        Rtot.draw('test.pdf')

        Rtot_2 = LSection(Rtota,Rtota)
        ans1 = Rtot_2.Y1sc
        print(ans1.simplify())
        ans2 = Rtot_2.Y2sc
        print(ans2.simplify())


if __name__ =='__main__':
    unittest.main()
