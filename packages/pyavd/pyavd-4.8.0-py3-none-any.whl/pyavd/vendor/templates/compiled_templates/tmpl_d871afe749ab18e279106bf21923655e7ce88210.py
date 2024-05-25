from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/dot1x.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_dot1x = resolve('dot1x')
    l_0_aaa_config = resolve('aaa_config')
    l_0_actions = resolve('actions')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x)):
        pass
        yield '!\n'
        if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'system_auth_control'), True):
            pass
            yield 'dot1x system-auth-control\n'
        if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'protocol_lldp_bypass'), True):
            pass
            yield 'dot1x protocol lldp bypass\n'
        if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'protocol_bpdu_bypass'), True):
            pass
            yield 'dot1x protocol bpdu bypass\n'
        if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'dynamic_authorization'), True):
            pass
            yield 'dot1x dynamic-authorization\n'
        if ((t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication')) or t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'))) or t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'))):
            pass
            yield 'dot1x\n'
            if t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive')):
                pass
                l_0_aaa_config = 'aaa unresponsive'
                context.vars['aaa_config'] = l_0_aaa_config
                context.exported_vars.add('aaa_config')
                if (t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), 'phone_action')) or t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), 'action'))):
                    pass
                    l_0_actions = [{'name': 'phone_action', 'config': str_join(((undefined(name='aaa_config') if l_0_aaa_config is missing else l_0_aaa_config), ' phone action', ))}, {'name': 'action', 'config': str_join(((undefined(name='aaa_config') if l_0_aaa_config is missing else l_0_aaa_config), ' action', ))}]
                    context.vars['actions'] = l_0_actions
                    context.exported_vars.add('actions')
                    for l_1_action in (undefined(name='actions') if l_0_actions is missing else l_0_actions):
                        l_1_aaa_action_config = resolve('aaa_action_config')
                        l_1_action_apply_config = resolve('action_apply_config')
                        l_1_traffic = resolve('traffic')
                        _loop_vars = {}
                        pass
                        if t_1(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name'))):
                            pass
                            l_1_aaa_action_config = environment.getattr(l_1_action, 'config')
                            _loop_vars['aaa_action_config'] = l_1_aaa_action_config
                            if ((t_1(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'apply_cached_results'), True) or t_1(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'traffic_allow'), True)) or t_1(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'traffic_allow_vlan'))):
                                pass
                                if t_1(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'apply_cached_results'), True):
                                    pass
                                    l_1_action_apply_config = 'apply cached-results'
                                    _loop_vars['action_apply_config'] = l_1_action_apply_config
                                    if (t_1(environment.getattr(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'cached_results_timeout'), 'time_duration')) and t_1(environment.getattr(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'cached_results_timeout'), 'time_duration_unit'))):
                                        pass
                                        l_1_action_apply_config = str_join(((undefined(name='action_apply_config') if l_1_action_apply_config is missing else l_1_action_apply_config), ' timeout ', environment.getattr(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'cached_results_timeout'), 'time_duration'), ' ', environment.getattr(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'cached_results_timeout'), 'time_duration_unit'), ))
                                        _loop_vars['action_apply_config'] = l_1_action_apply_config
                                if t_1(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'traffic_allow'), True):
                                    pass
                                    l_1_traffic = 'traffic allow'
                                    _loop_vars['traffic'] = l_1_traffic
                                elif t_1(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'traffic_allow_vlan')):
                                    pass
                                    l_1_traffic = str_join(('traffic allow vlan ', environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'traffic_allow_vlan'), ))
                                    _loop_vars['traffic'] = l_1_traffic
                                if ((t_1(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'apply_alternate'), True) and t_1((undefined(name='action_apply_config') if l_1_action_apply_config is missing else l_1_action_apply_config))) and t_1((undefined(name='traffic') if l_1_traffic is missing else l_1_traffic))):
                                    pass
                                    l_1_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_1_aaa_action_config is missing else l_1_aaa_action_config), ' ', (undefined(name='action_apply_config') if l_1_action_apply_config is missing else l_1_action_apply_config), ' else ', (undefined(name='traffic') if l_1_traffic is missing else l_1_traffic), ))
                                    _loop_vars['aaa_action_config'] = l_1_aaa_action_config
                                elif t_1((undefined(name='action_apply_config') if l_1_action_apply_config is missing else l_1_action_apply_config)):
                                    pass
                                    l_1_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_1_aaa_action_config is missing else l_1_aaa_action_config), ' ', (undefined(name='action_apply_config') if l_1_action_apply_config is missing else l_1_action_apply_config), ))
                                    _loop_vars['aaa_action_config'] = l_1_aaa_action_config
                                elif t_1((undefined(name='traffic') if l_1_traffic is missing else l_1_traffic)):
                                    pass
                                    l_1_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_1_aaa_action_config is missing else l_1_aaa_action_config), ' ', (undefined(name='traffic') if l_1_traffic is missing else l_1_traffic), ))
                                    _loop_vars['aaa_action_config'] = l_1_aaa_action_config
                                yield '   '
                                yield str((undefined(name='aaa_action_config') if l_1_aaa_action_config is missing else l_1_aaa_action_config))
                                yield '\n'
                    l_1_action = l_1_aaa_action_config = l_1_action_apply_config = l_1_traffic = missing
                if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), 'eap_response')):
                    pass
                    yield '   '
                    yield str((undefined(name='aaa_config') if l_0_aaa_config is missing else l_0_aaa_config))
                    yield ' eap response '
                    yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), 'eap_response'))
                    yield '\n'
                if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), 'recovery_action_reauthenticate'), True):
                    pass
                    yield '   '
                    yield str((undefined(name='aaa_config') if l_0_aaa_config is missing else l_0_aaa_config))
                    yield ' recovery action reauthenticate\n'
            if t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'accounting_update_interval')):
                pass
                yield '   aaa accounting update interval '
                yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'accounting_update_interval'))
                yield ' seconds\n'
            if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication')):
                pass
                if t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'delay')):
                    pass
                    yield '   mac based authentication delay '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'delay'))
                    yield ' seconds\n'
                if t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'hold_period')):
                    pass
                    yield '   mac based authentication hold period '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'hold_period'))
                    yield ' seconds\n'
            if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair')):
                pass
                if t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'service_type'), True):
                    pass
                    yield '   radius av-pair service-type\n'
                if t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'framed_mtu')):
                    pass
                    yield '   radius av-pair framed-mtu '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'framed_mtu'))
                    yield '\n'

blocks = {}
debug_info = '7=20&9=23&12=26&15=29&18=32&21=35&23=38&24=40&25=43&26=45&27=48&28=54&29=56&30=58&33=60&34=62&35=64&36=66&39=68&40=70&41=72&42=74&44=76&45=78&46=80&47=82&48=84&49=86&51=89&56=92&57=95&59=99&60=102&63=104&64=107&66=109&67=111&68=114&70=116&71=119&74=121&75=123&78=126&79=129'