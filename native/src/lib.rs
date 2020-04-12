#![feature(asm)]
#[macro_use]
extern crate neon;
extern crate probe;

use neon::prelude::*;
use probe::*;

fn hello(mut cx: FunctionContext) -> JsResult<JsString> {
        probe!(foo, helloprobe);
        Ok(cx.string("hello node"))
}

register_module!(mut cx, {
    cx.export_function("hello", hello)
});

