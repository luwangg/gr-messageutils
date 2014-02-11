# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_messageutils_swig', [dirname(__file__)])
        except ImportError:
            import _messageutils_swig
            return _messageutils_swig
        if fp is not None:
            try:
                _mod = imp.load_module('_messageutils_swig', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _messageutils_swig = swig_import_helper()
    del swig_import_helper
else:
    import _messageutils_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now():
  """high_res_timer_now() -> high_res_timer_type"""
  return _messageutils_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
  """high_res_timer_now_perfmon() -> high_res_timer_type"""
  return _messageutils_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
  """high_res_timer_tps() -> high_res_timer_type"""
  return _messageutils_swig.high_res_timer_tps()

def high_res_timer_epoch():
  """high_res_timer_epoch() -> high_res_timer_type"""
  return _messageutils_swig.high_res_timer_epoch()
class pdu_debug(object):
    """
    Debug block with added functions for PDUs.

    The message debug block is used to capture and print or store messages as they are received. Any block that generates a message may connect that message port to one or more of the three message input ports of this debug block. The message ports are:
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def make(*args, **kwargs):
        """
        make(bool meta_only) -> sptr

        Params: (meta_only)
        """
        return _messageutils_swig.pdu_debug_make(*args, **kwargs)

    make = staticmethod(make)
    __swig_destroy__ = _messageutils_swig.delete_pdu_debug
    __del__ = lambda self : None;
pdu_debug_swigregister = _messageutils_swig.pdu_debug_swigregister
pdu_debug_swigregister(pdu_debug)

def pdu_debug_make(*args, **kwargs):
  """
    pdu_debug_make(bool meta_only) -> sptr

    Params: (meta_only)
    """
  return _messageutils_swig.pdu_debug_make(*args, **kwargs)

class pdu_debug_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::messageutils::pdu_debug)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> pdu_debug_sptr
        __init__(self, pdu_debug p) -> pdu_debug_sptr
        """
        this = _messageutils_swig.new_pdu_debug_sptr(*args)
        try: self.this.append(this)
        except: self.this = this
    def __deref__(self):
        """__deref__(self) -> pdu_debug"""
        return _messageutils_swig.pdu_debug_sptr___deref__(self)

    __swig_destroy__ = _messageutils_swig.delete_pdu_debug_sptr
    __del__ = lambda self : None;
    def make(self, *args, **kwargs):
        """
        make(self, bool meta_only) -> sptr

        Params: (meta_only)
        """
        return _messageutils_swig.pdu_debug_sptr_make(self, *args, **kwargs)

    def history(self):
        """history(self) -> unsigned int"""
        return _messageutils_swig.pdu_debug_sptr_history(self)

    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(self, int which, int delay)
        declare_sample_delay(self, unsigned int delay)
        """
        return _messageutils_swig.pdu_debug_sptr_declare_sample_delay(self, *args)

    def sample_delay(self, *args, **kwargs):
        """sample_delay(self, int which) -> unsigned int"""
        return _messageutils_swig.pdu_debug_sptr_sample_delay(self, *args, **kwargs)

    def output_multiple(self):
        """output_multiple(self) -> int"""
        return _messageutils_swig.pdu_debug_sptr_output_multiple(self)

    def relative_rate(self):
        """relative_rate(self) -> double"""
        return _messageutils_swig.pdu_debug_sptr_relative_rate(self)

    def start(self):
        """start(self) -> bool"""
        return _messageutils_swig.pdu_debug_sptr_start(self)

    def stop(self):
        """stop(self) -> bool"""
        return _messageutils_swig.pdu_debug_sptr_stop(self)

    def nitems_read(self, *args, **kwargs):
        """nitems_read(self, unsigned int which_input) -> uint64_t"""
        return _messageutils_swig.pdu_debug_sptr_nitems_read(self, *args, **kwargs)

    def nitems_written(self, *args, **kwargs):
        """nitems_written(self, unsigned int which_output) -> uint64_t"""
        return _messageutils_swig.pdu_debug_sptr_nitems_written(self, *args, **kwargs)

    def max_noutput_items(self):
        """max_noutput_items(self) -> int"""
        return _messageutils_swig.pdu_debug_sptr_max_noutput_items(self)

    def set_max_noutput_items(self, *args, **kwargs):
        """set_max_noutput_items(self, int m)"""
        return _messageutils_swig.pdu_debug_sptr_set_max_noutput_items(self, *args, **kwargs)

    def unset_max_noutput_items(self):
        """unset_max_noutput_items(self)"""
        return _messageutils_swig.pdu_debug_sptr_unset_max_noutput_items(self)

    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(self) -> bool"""
        return _messageutils_swig.pdu_debug_sptr_is_set_max_noutput_items(self)

    def max_output_buffer(self, *args, **kwargs):
        """max_output_buffer(self, int i) -> long"""
        return _messageutils_swig.pdu_debug_sptr_max_output_buffer(self, *args, **kwargs)

    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(self, long max_output_buffer)
        set_max_output_buffer(self, int port, long max_output_buffer)
        """
        return _messageutils_swig.pdu_debug_sptr_set_max_output_buffer(self, *args)

    def min_output_buffer(self, *args, **kwargs):
        """min_output_buffer(self, int i) -> long"""
        return _messageutils_swig.pdu_debug_sptr_min_output_buffer(self, *args, **kwargs)

    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(self, long min_output_buffer)
        set_min_output_buffer(self, int port, long min_output_buffer)
        """
        return _messageutils_swig.pdu_debug_sptr_set_min_output_buffer(self, *args)

    def pc_noutput_items(self):
        """pc_noutput_items(self) -> float"""
        return _messageutils_swig.pdu_debug_sptr_pc_noutput_items(self)

    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(self) -> float"""
        return _messageutils_swig.pdu_debug_sptr_pc_noutput_items_avg(self)

    def pc_noutput_items_var(self):
        """pc_noutput_items_var(self) -> float"""
        return _messageutils_swig.pdu_debug_sptr_pc_noutput_items_var(self)

    def pc_nproduced(self):
        """pc_nproduced(self) -> float"""
        return _messageutils_swig.pdu_debug_sptr_pc_nproduced(self)

    def pc_nproduced_avg(self):
        """pc_nproduced_avg(self) -> float"""
        return _messageutils_swig.pdu_debug_sptr_pc_nproduced_avg(self)

    def pc_nproduced_var(self):
        """pc_nproduced_var(self) -> float"""
        return _messageutils_swig.pdu_debug_sptr_pc_nproduced_var(self)

    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(self, int which) -> float
        pc_input_buffers_full(self) -> pmt_vector_float
        """
        return _messageutils_swig.pdu_debug_sptr_pc_input_buffers_full(self, *args)

    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(self, int which) -> float
        pc_input_buffers_full_avg(self) -> pmt_vector_float
        """
        return _messageutils_swig.pdu_debug_sptr_pc_input_buffers_full_avg(self, *args)

    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(self, int which) -> float
        pc_input_buffers_full_var(self) -> pmt_vector_float
        """
        return _messageutils_swig.pdu_debug_sptr_pc_input_buffers_full_var(self, *args)

    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(self, int which) -> float
        pc_output_buffers_full(self) -> pmt_vector_float
        """
        return _messageutils_swig.pdu_debug_sptr_pc_output_buffers_full(self, *args)

    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(self, int which) -> float
        pc_output_buffers_full_avg(self) -> pmt_vector_float
        """
        return _messageutils_swig.pdu_debug_sptr_pc_output_buffers_full_avg(self, *args)

    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(self, int which) -> float
        pc_output_buffers_full_var(self) -> pmt_vector_float
        """
        return _messageutils_swig.pdu_debug_sptr_pc_output_buffers_full_var(self, *args)

    def pc_work_time(self):
        """pc_work_time(self) -> float"""
        return _messageutils_swig.pdu_debug_sptr_pc_work_time(self)

    def pc_work_time_avg(self):
        """pc_work_time_avg(self) -> float"""
        return _messageutils_swig.pdu_debug_sptr_pc_work_time_avg(self)

    def pc_work_time_var(self):
        """pc_work_time_var(self) -> float"""
        return _messageutils_swig.pdu_debug_sptr_pc_work_time_var(self)

    def pc_work_time_total(self):
        """pc_work_time_total(self) -> float"""
        return _messageutils_swig.pdu_debug_sptr_pc_work_time_total(self)

    def set_processor_affinity(self, *args, **kwargs):
        """set_processor_affinity(self, __dummy_5__ mask)"""
        return _messageutils_swig.pdu_debug_sptr_set_processor_affinity(self, *args, **kwargs)

    def unset_processor_affinity(self):
        """unset_processor_affinity(self)"""
        return _messageutils_swig.pdu_debug_sptr_unset_processor_affinity(self)

    def processor_affinity(self):
        """processor_affinity(self) -> __dummy_5__"""
        return _messageutils_swig.pdu_debug_sptr_processor_affinity(self)

    def active_thread_priority(self):
        """active_thread_priority(self) -> int"""
        return _messageutils_swig.pdu_debug_sptr_active_thread_priority(self)

    def thread_priority(self):
        """thread_priority(self) -> int"""
        return _messageutils_swig.pdu_debug_sptr_thread_priority(self)

    def set_thread_priority(self, *args, **kwargs):
        """set_thread_priority(self, int priority) -> int"""
        return _messageutils_swig.pdu_debug_sptr_set_thread_priority(self, *args, **kwargs)

    def name(self):
        """name(self) -> string"""
        return _messageutils_swig.pdu_debug_sptr_name(self)

    def symbol_name(self):
        """symbol_name(self) -> string"""
        return _messageutils_swig.pdu_debug_sptr_symbol_name(self)

    def input_signature(self):
        """input_signature(self) -> sptr"""
        return _messageutils_swig.pdu_debug_sptr_input_signature(self)

    def output_signature(self):
        """output_signature(self) -> sptr"""
        return _messageutils_swig.pdu_debug_sptr_output_signature(self)

    def unique_id(self):
        """unique_id(self) -> long"""
        return _messageutils_swig.pdu_debug_sptr_unique_id(self)

    def to_basic_block(self):
        """to_basic_block(self) -> basic_block_sptr"""
        return _messageutils_swig.pdu_debug_sptr_to_basic_block(self)

    def check_topology(self, *args, **kwargs):
        """check_topology(self, int ninputs, int noutputs) -> bool"""
        return _messageutils_swig.pdu_debug_sptr_check_topology(self, *args, **kwargs)

    def alias(self):
        """alias(self) -> string"""
        return _messageutils_swig.pdu_debug_sptr_alias(self)

    def set_block_alias(self, *args, **kwargs):
        """set_block_alias(self, string name)"""
        return _messageutils_swig.pdu_debug_sptr_set_block_alias(self, *args, **kwargs)

    def _post(self, *args, **kwargs):
        """_post(self, pmt_t which_port, pmt_t msg)"""
        return _messageutils_swig.pdu_debug_sptr__post(self, *args, **kwargs)

    def message_ports_in(self):
        """message_ports_in(self) -> pmt_t"""
        return _messageutils_swig.pdu_debug_sptr_message_ports_in(self)

    def message_ports_out(self):
        """message_ports_out(self) -> pmt_t"""
        return _messageutils_swig.pdu_debug_sptr_message_ports_out(self)

    def message_subscribers(self, *args, **kwargs):
        """message_subscribers(self, pmt_t which_port) -> pmt_t"""
        return _messageutils_swig.pdu_debug_sptr_message_subscribers(self, *args, **kwargs)

pdu_debug_sptr_swigregister = _messageutils_swig.pdu_debug_sptr_swigregister
pdu_debug_sptr_swigregister(pdu_debug_sptr)

pdu_debug_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
pdu_debug = pdu_debug.make;



