from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/event-handlers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_event_handlers = resolve('event_handlers')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_3 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_4 = environment.filters['replace']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'replace' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_5((undefined(name='event_handlers') if l_0_event_handlers is missing else l_0_event_handlers)):
        pass
        yield '\n### Event Handler\n\n#### Event Handler Summary\n\n| Handler | Actions | Trigger | Trigger Config |\n| ------- | ------- | ------- | -------------- |\n'
        for l_1_handler in t_2((undefined(name='event_handlers') if l_0_event_handlers is missing else l_0_event_handlers), 'name'):
            l_1_actions = resolve('actions')
            l_1_action = resolve('action')
            l_1_bash_command = resolve('bash_command')
            l_1_metric = resolve('metric')
            l_1_trigger_config = resolve('trigger_config')
            _loop_vars = {}
            pass
            if t_5(environment.getattr(l_1_handler, 'action_type')):
                pass
                l_1_actions = environment.getattr(l_1_handler, 'action_type')
                _loop_vars['actions'] = l_1_actions
                if t_5(environment.getattr(l_1_handler, 'action')):
                    pass
                    l_1_action = t_4(context.eval_ctx, environment.getattr(l_1_handler, 'action'), '|', '\\|')
                    _loop_vars['action'] = l_1_action
                    l_1_actions = str_join(((undefined(name='actions') if l_1_actions is missing else l_1_actions), ' <code>', (undefined(name='action') if l_1_action is missing else l_1_action), '</code>', ))
                    _loop_vars['actions'] = l_1_actions
            if t_5(environment.getattr(l_1_handler, 'actions')):
                pass
                l_1_actions = []
                _loop_vars['actions'] = l_1_actions
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'bash_command')):
                    pass
                    l_1_bash_command = t_4(context.eval_ctx, t_4(context.eval_ctx, environment.getattr(environment.getattr(l_1_handler, 'actions'), 'bash_command'), '\n', '\\n'), '|', '\\|')
                    _loop_vars['bash_command'] = l_1_bash_command
                    l_1_bash_command = str_join(('<code>', (undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), '</code>', ))
                    _loop_vars['bash_command'] = l_1_bash_command
                    l_1_bash_command = str_join(('bash ', (undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), ))
                    _loop_vars['bash_command'] = l_1_bash_command
                    context.call(environment.getattr((undefined(name='actions') if l_1_actions is missing else l_1_actions), 'append'), (undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), _loop_vars=_loop_vars)
                elif t_5(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'log')):
                    pass
                    context.call(environment.getattr((undefined(name='actions') if l_1_actions is missing else l_1_actions), 'append'), 'log', _loop_vars=_loop_vars)
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'increment_device_health_metric')):
                    pass
                    l_1_metric = str_join(('increment device health metric ', environment.getattr(environment.getattr(l_1_handler, 'actions'), 'increment_device_health_metric'), ))
                    _loop_vars['metric'] = l_1_metric
                    context.call(environment.getattr((undefined(name='actions') if l_1_actions is missing else l_1_actions), 'append'), (undefined(name='metric') if l_1_metric is missing else l_1_metric), _loop_vars=_loop_vars)
                l_1_actions = t_3(context.eval_ctx, (undefined(name='actions') if l_1_actions is missing else l_1_actions), '<br>')
                _loop_vars['actions'] = l_1_actions
            if ((t_5(environment.getattr(l_1_handler, 'trigger'), 'on-maintenance') and t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'operation'))) and t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'))):
                pass
                l_1_trigger_config = str_join(('trigger ', environment.getattr(l_1_handler, 'trigger'), ' ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'operation'), ))
                _loop_vars['trigger_config'] = l_1_trigger_config
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'bgp_peer')):
                    pass
                    l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' bgp ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'bgp_peer'), ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
                    if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'vrf')):
                        pass
                        l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' vrf ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'vrf'), ))
                        _loop_vars['trigger_config'] = l_1_trigger_config
                elif t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'interface')):
                    pass
                    l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' interface ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'interface'), ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
                elif t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'unit')):
                    pass
                    l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' unit ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'unit'), ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
                if (t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), 'after') or t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), 'before')):
                    pass
                    l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), ' stage ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'stage'), ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
                elif t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), 'all'):
                    pass
                    l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' all', ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
                elif t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), 'begin'):
                    pass
                    l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' begin', ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
                elif t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), 'end'):
                    pass
                    l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' end', ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
            elif t_5(environment.getattr(l_1_handler, 'trigger'), 'on-counters'):
                pass
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'poll_interval')):
                    pass
                    l_1_trigger_config = str_join(('poll interval ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'poll_interval'), ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'condition')):
                    pass
                    l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), '<br>condition', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'condition'), ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'granularity_per_source'), True):
                    pass
                    l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), '<br>granularity per-source', ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
            elif t_5(environment.getattr(l_1_handler, 'trigger'), 'on-logging'):
                pass
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'poll_interval')):
                    pass
                    l_1_trigger_config = str_join(('poll interval ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'poll_interval'), ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'regex')):
                    pass
                    l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), '<br>regex ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'regex'), ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
            elif (t_5(environment.getattr(l_1_handler, 'trigger'), 'on-intf') and t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'interface'))):
                pass
                if ((t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ip'), True) or t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ipv6'), True)) or t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'operstatus'), True)):
                    pass
                    l_1_trigger_config = str_join(('trigger on-intf ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'interface'), ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
                    if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'operstatus'), True):
                        pass
                        l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' operstatus', ))
                        _loop_vars['trigger_config'] = l_1_trigger_config
                    if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ip'), True):
                        pass
                        l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' ip', ))
                        _loop_vars['trigger_config'] = l_1_trigger_config
                    if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ipv6'), True):
                        pass
                        l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' ip6', ))
                        _loop_vars['trigger_config'] = l_1_trigger_config
            yield '| '
            yield str(environment.getattr(l_1_handler, 'name'))
            yield ' | '
            yield str(t_1((undefined(name='actions') if l_1_actions is missing else l_1_actions), '-'))
            yield ' | '
            yield str(t_1(environment.getattr(l_1_handler, 'trigger'), '-'))
            yield ' | '
            yield str(t_1((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), '-'))
            yield ' |\n'
        l_1_handler = l_1_actions = l_1_action = l_1_bash_command = l_1_metric = l_1_trigger_config = missing
        yield '\n#### Event Handler Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/event-handlers.j2', 'documentation/event-handlers.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=42&15=45&16=53&17=55&18=57&19=59&20=61&23=63&24=65&25=67&26=69&27=71&28=73&29=75&30=76&31=78&33=79&34=81&35=83&37=84&39=86&42=88&43=90&44=92&45=94&46=96&48=98&49=100&50=102&51=104&53=106&54=108&55=110&56=112&57=114&58=116&59=118&60=120&62=122&63=124&64=126&66=128&67=130&69=132&70=134&72=136&73=138&74=140&76=142&77=144&79=146&80=148&83=150&84=152&85=154&87=156&88=158&90=160&91=162&95=165&101=175'