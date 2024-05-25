from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/event-handlers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_event_handlers = resolve('event_handlers')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['indent']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'indent' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='event_handlers') if l_0_event_handlers is missing else l_0_event_handlers)):
        pass
        for l_1_handler in t_1((undefined(name='event_handlers') if l_0_event_handlers is missing else l_0_event_handlers), 'name'):
            l_1_trigger_on_manitenance_cli = resolve('trigger_on_manitenance_cli')
            l_1_trigger_on_intf_cli = resolve('trigger_on_intf_cli')
            l_1_bash_command = resolve('bash_command')
            _loop_vars = {}
            pass
            yield '!\nevent-handler '
            yield str(environment.getattr(l_1_handler, 'name'))
            yield '\n'
            if t_3(environment.getattr(l_1_handler, 'trigger')):
                pass
                if ((t_3(environment.getattr(l_1_handler, 'trigger'), 'on-maintenance') and t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'operation'))) and t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'))):
                    pass
                    l_1_trigger_on_manitenance_cli = str_join(('trigger ', environment.getattr(l_1_handler, 'trigger'), ' ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'operation'), ))
                    _loop_vars['trigger_on_manitenance_cli'] = l_1_trigger_on_manitenance_cli
                    if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'bgp_peer')):
                        pass
                        l_1_trigger_on_manitenance_cli = str_join(((undefined(name='trigger_on_manitenance_cli') if l_1_trigger_on_manitenance_cli is missing else l_1_trigger_on_manitenance_cli), ' bgp ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'bgp_peer'), ))
                        _loop_vars['trigger_on_manitenance_cli'] = l_1_trigger_on_manitenance_cli
                        if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'vrf')):
                            pass
                            l_1_trigger_on_manitenance_cli = str_join(((undefined(name='trigger_on_manitenance_cli') if l_1_trigger_on_manitenance_cli is missing else l_1_trigger_on_manitenance_cli), ' vrf ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'vrf'), ))
                            _loop_vars['trigger_on_manitenance_cli'] = l_1_trigger_on_manitenance_cli
                    elif t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'interface')):
                        pass
                        l_1_trigger_on_manitenance_cli = str_join(((undefined(name='trigger_on_manitenance_cli') if l_1_trigger_on_manitenance_cli is missing else l_1_trigger_on_manitenance_cli), ' interface ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'interface'), ))
                        _loop_vars['trigger_on_manitenance_cli'] = l_1_trigger_on_manitenance_cli
                    elif t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'unit')):
                        pass
                        l_1_trigger_on_manitenance_cli = str_join(((undefined(name='trigger_on_manitenance_cli') if l_1_trigger_on_manitenance_cli is missing else l_1_trigger_on_manitenance_cli), ' unit ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'unit'), ))
                        _loop_vars['trigger_on_manitenance_cli'] = l_1_trigger_on_manitenance_cli
                    if (t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), 'after') or t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), 'before')):
                        pass
                        l_1_trigger_on_manitenance_cli = str_join(((undefined(name='trigger_on_manitenance_cli') if l_1_trigger_on_manitenance_cli is missing else l_1_trigger_on_manitenance_cli), ' ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), ' stage ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'stage'), ))
                        _loop_vars['trigger_on_manitenance_cli'] = l_1_trigger_on_manitenance_cli
                    elif t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), 'all'):
                        pass
                        l_1_trigger_on_manitenance_cli = str_join(((undefined(name='trigger_on_manitenance_cli') if l_1_trigger_on_manitenance_cli is missing else l_1_trigger_on_manitenance_cli), ' all', ))
                        _loop_vars['trigger_on_manitenance_cli'] = l_1_trigger_on_manitenance_cli
                    elif t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), 'begin'):
                        pass
                        l_1_trigger_on_manitenance_cli = str_join(((undefined(name='trigger_on_manitenance_cli') if l_1_trigger_on_manitenance_cli is missing else l_1_trigger_on_manitenance_cli), ' begin', ))
                        _loop_vars['trigger_on_manitenance_cli'] = l_1_trigger_on_manitenance_cli
                    elif t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), 'end'):
                        pass
                        l_1_trigger_on_manitenance_cli = str_join(((undefined(name='trigger_on_manitenance_cli') if l_1_trigger_on_manitenance_cli is missing else l_1_trigger_on_manitenance_cli), ' end', ))
                        _loop_vars['trigger_on_manitenance_cli'] = l_1_trigger_on_manitenance_cli
                    yield '   '
                    yield str((undefined(name='trigger_on_manitenance_cli') if l_1_trigger_on_manitenance_cli is missing else l_1_trigger_on_manitenance_cli))
                    yield '\n'
                elif t_3(environment.getattr(l_1_handler, 'trigger'), 'on-counters'):
                    pass
                    yield '   trigger on-counters\n'
                    if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'poll_interval')):
                        pass
                        yield '      poll interval '
                        yield str(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'poll_interval'))
                        yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'condition')):
                        pass
                        yield '      condition '
                        yield str(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'condition'))
                        yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'granularity_per_source'), True):
                        pass
                        yield '      granularity per-source\n'
                elif t_3(environment.getattr(l_1_handler, 'trigger'), 'on-logging'):
                    pass
                    yield '   trigger on-logging\n'
                    if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'poll_interval')):
                        pass
                        yield '      poll interval '
                        yield str(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'poll_interval'))
                        yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'regex')):
                        pass
                        yield '      regex '
                        yield str(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'regex'))
                        yield '\n'
                elif (t_3(environment.getattr(l_1_handler, 'trigger'), 'on-intf') and t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'interface'))):
                    pass
                    if ((t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ip'), True) or t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ipv6'), True)) or t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'operstatus'), True)):
                        pass
                        l_1_trigger_on_intf_cli = str_join(('trigger on-intf ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'interface'), ))
                        _loop_vars['trigger_on_intf_cli'] = l_1_trigger_on_intf_cli
                        if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'operstatus'), True):
                            pass
                            l_1_trigger_on_intf_cli = str_join(((undefined(name='trigger_on_intf_cli') if l_1_trigger_on_intf_cli is missing else l_1_trigger_on_intf_cli), ' operstatus', ))
                            _loop_vars['trigger_on_intf_cli'] = l_1_trigger_on_intf_cli
                        if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ip'), True):
                            pass
                            l_1_trigger_on_intf_cli = str_join(((undefined(name='trigger_on_intf_cli') if l_1_trigger_on_intf_cli is missing else l_1_trigger_on_intf_cli), ' ip', ))
                            _loop_vars['trigger_on_intf_cli'] = l_1_trigger_on_intf_cli
                        if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ipv6'), True):
                            pass
                            l_1_trigger_on_intf_cli = str_join(((undefined(name='trigger_on_intf_cli') if l_1_trigger_on_intf_cli is missing else l_1_trigger_on_intf_cli), ' ip6', ))
                            _loop_vars['trigger_on_intf_cli'] = l_1_trigger_on_intf_cli
                        yield '   '
                        yield str((undefined(name='trigger_on_intf_cli') if l_1_trigger_on_intf_cli is missing else l_1_trigger_on_intf_cli))
                        yield '\n'
                else:
                    pass
                    yield '   trigger '
                    yield str(environment.getattr(l_1_handler, 'trigger'))
                    yield '\n'
                if t_3(environment.getattr(l_1_handler, 'regex')):
                    pass
                    yield '      regex '
                    yield str(environment.getattr(l_1_handler, 'regex'))
                    yield '\n'
            if (t_3(environment.getattr(l_1_handler, 'action')) and t_3(environment.getattr(l_1_handler, 'action_type'))):
                pass
                yield '   action '
                yield str(environment.getattr(l_1_handler, 'action_type'))
                yield ' '
                yield str(environment.getattr(l_1_handler, 'action'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'bash_command')):
                pass
                l_1_bash_command = environment.getattr(environment.getattr(l_1_handler, 'actions'), 'bash_command')
                _loop_vars['bash_command'] = l_1_bash_command
                if (context.call(environment.getattr((undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), 'count'), '\n', _loop_vars=_loop_vars) > 0):
                    pass
                    if (not context.call(environment.getattr(context.call(environment.getattr((undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), 'rstrip'), _loop_vars=_loop_vars), 'endswith'), '\nEOF', _loop_vars=_loop_vars)):
                        pass
                        l_1_bash_command = str_join((context.call(environment.getattr((undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), 'rstrip'), _loop_vars=_loop_vars), '\nEOF', ))
                        _loop_vars['bash_command'] = l_1_bash_command
                    yield '   action bash\n      '
                    yield str(t_2((undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), width=6, first=False))
                    yield '\n'
                else:
                    pass
                    yield '   action bash '
                    yield str((undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command))
                    yield '\n'
            elif t_3(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'log'), True):
                pass
                yield '   action log\n'
            if t_3(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'increment_device_health_metric')):
                pass
                yield '   action increment device-health metric '
                yield str(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'increment_device_health_metric'))
                yield '\n'
            if t_3(environment.getattr(l_1_handler, 'delay')):
                pass
                yield '   delay '
                yield str(environment.getattr(l_1_handler, 'delay'))
                yield '\n'
            if t_3(environment.getattr(l_1_handler, 'asynchronous'), True):
                pass
                yield '   asynchronous\n'
        l_1_handler = l_1_trigger_on_manitenance_cli = l_1_trigger_on_intf_cli = l_1_bash_command = missing

blocks = {}
debug_info = '7=30&8=32&10=39&11=41&12=43&15=45&16=47&17=49&18=51&19=53&21=55&22=57&23=59&24=61&26=63&27=65&28=67&29=69&30=71&31=73&32=75&33=77&35=80&36=82&38=85&39=88&41=90&42=93&44=95&47=98&49=101&50=104&52=106&53=109&55=111&56=113&59=115&60=117&61=119&63=121&64=123&66=125&67=127&69=130&72=135&74=137&75=140&78=142&79=145&81=149&82=151&83=153&84=155&85=157&88=160&90=165&92=167&95=170&96=173&98=175&99=178&101=180'