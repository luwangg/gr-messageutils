/* -*- c++ -*- */
/* 
 * Copyright 2017 <+YOU OR YOUR COMPANY+>.
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

#ifndef INCLUDED_MESSAGEUTILS_PDU_TO_FILE_IMPL_H
#define INCLUDED_MESSAGEUTILS_PDU_TO_FILE_IMPL_H

#include <messageutils/pdu_to_file.h>

namespace gr {
  namespace messageutils {

    class pdu_to_file_impl : public pdu_to_file
    {
     private:
     	size_t d_itemsize;
     	bool	 d_debug;

     public:
      pdu_to_file_impl(const char *filename, bool append, bool debug);
      ~pdu_to_file_impl();

			void handle_msg(pmt::pmt_t msg);

    };

  } // namespace messageutils
} // namespace gr

#endif /* INCLUDED_MESSAGEUTILS_PDU_TO_FILE_IMPL_H */

