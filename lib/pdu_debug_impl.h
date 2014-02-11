/* -*- c++ -*- */
/* 
 * Copyright 2014 Adam Gannon.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_MESSAGEUTILS_PDU_DEBUG_IMPL_H
#define INCLUDED_MESSAGEUTILS_PDU_DEBUG_IMPL_H

#include <messageutils/pdu_debug.h>

namespace gr {
  namespace messageutils {

    class pdu_debug_impl : public pdu_debug
    {
     private:
      gr::thread::mutex d_mutex;
      std::vector<pmt::pmt_t> d_messages;
      bool d_meta_only;

     public:
      pdu_debug_impl(bool meta_only);
      ~pdu_debug_impl();


      void print_pdu(pmt::pmt_t pdu);
      int num_messages();
      pmt::pmt_t get_message(int i);

      // Where all the action really happens
    


    };

  } // namespace messageutils
} // namespace gr

#endif /* INCLUDED_MESSAGEUTILS_PDU_DEBUG_IMPL_H */
